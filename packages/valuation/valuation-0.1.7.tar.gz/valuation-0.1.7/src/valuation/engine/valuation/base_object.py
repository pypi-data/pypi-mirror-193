from __future__ import annotations

import contextlib
import math
from collections import OrderedDict, defaultdict
from dataclasses import dataclass
from functools import singledispatch
from typing import Any, ContextManager, Generator, Iterable, Optional, Union

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine import QLObject
from valuation.engine.check import ContainedIn, ObjectType, Range, RangeWarning
from valuation.engine.exceptions import DAARuntimeException
from valuation.engine.market_data import QLMarketData
from valuation.engine.utils import CashFlows, PVDescriptor, qldate2date, AdditionalBondCfInfo
from valuation.universal_output import ResultLineAmount, ResultLineCleanDirty, ResultLineFlexible, ResultLineGreek, \
    ResultLineInfo, ResultLinePV, ResultLineRange, ResultLineSimpleCashFlow
from valuation.universal_output import result_items
from valuation.universal_output.result import ResultLineBondAdditionalInfo
from valuation.universal_transfer import NoValue, Reference, Signature

if __type_checking__:
    # pylint: disable=ungrouped-imports
    import datetime
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument import QLInstrument
    from valuation.engine.market_data import QLYieldCurve
    from valuation.universal_transfer import DefaultParameters, Storage


class QLValuationBase(QLObject):
    _valuation_type: Optional[str] = 'ERROR'
    _allowed_greeks: list[str] = result_items.AllGreeks


# todo: we need a mechanism that allows the communication between valuation and from valuation to instrument, that
#   is able to give info, if a valuation  / instrument supports a specific result type


def combine_ids(id1: Optional[str], id2: Optional[str]) -> Optional[str]:
    if not id1:
        return id2 or None
    if not id2:
        return id1
    return f'{id1}|{id2}'


def collect_single_or_curve_stack(market_data_references: Iterable[Reference], ql_db: QLObjectDB,
                                  simultaneous_curve_shift: bool) -> Generator[Union[QLMarketData, tuple[QLMarketData, ...]], None, None]:
    def grouping_rule(market_data_reference: Reference) -> Reference:
        if simultaneous_curve_shift and market_data_reference.type == signatures.yield_curve.all.type:
            curve: QLYieldCurve = ql_db[market_data_reference]  # type: ignore[assignment]
            if curve.is_base_curve:
                return Reference(signatures.yield_curve.all.type, 'ALL')
        return market_data_reference

    groups: dict[Reference, list[QLMarketData]] = defaultdict(list)
    for reference in market_data_references:
        market_data_object: QLMarketData = ql_db[reference]  # type: ignore[assignment]
        groups[grouping_rule(reference)].append(market_data_object)
    for _, market_data in groups.items():
        if len(market_data) == 1:
            yield market_data[0]
        else:
            yield tuple(market_data)


@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)
class ShiftDescriptor:

    @property
    def shift(self) -> float:
        raise NotImplementedError

    @property
    def divisor(self) -> float:
        raise NotImplementedError

    def mirror_shift(self) -> ShiftDescriptor:
        raise NotImplementedError

    def get_context(self) -> Generator[ContextManager[None], None, None]:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)
class ShiftDescriptorSingle(ShiftDescriptor):  # pylint: disable=abstract-method
    market_data: QLMarketData


@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)
class GreekShift(ShiftDescriptorSingle):  # pylint: disable=abstract-method
    greek: str
    scenario: str
    _shift: float

    @property
    def divisor(self) -> float:
        return abs(self.market_data.scenario_divisor)

    @property
    def shift(self) -> float:
        return self._shift

    @property
    def unit(self) -> str:
        return result_items.Units[self.market_data.shift_unit]

    def mirror_shift(self) -> GreekShift:
        return GreekShift(self.market_data, self.greek, self.scenario, -self.shift)

    def get_context(self) -> Generator[ContextManager[None], None, None]:
        yield self.market_data.change_to(self.scenario, self.shift)

    def __str__(self) -> str:
        return str(self.market_data.reference.id)


@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)
class MarketDataShift(ShiftDescriptorSingle):  # pylint: disable=abstract-method
    is_high: bool = True

    @property
    def scenario(self) -> str:
        return 'high' if self.is_high else 'low'

    def mirror_shift(self) -> MarketDataShift:
        return MarketDataShift(self.market_data, not self.is_high)

    def get_context(self) -> Generator[ContextManager[None], None, None]:
        yield self.market_data.market_shift(self.scenario)

    def __str__(self) -> str:
        return f'{self.market_data.reference.id} {self.scenario}'


@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)
class StackedCurveShift(ShiftDescriptor):
    curve_descriptors: tuple[Union[GreekShift, MarketDataShift], ...]

    @property
    def is_greek_shift(self) -> bool:
        return isinstance(list(self.curve_descriptors)[0], GreekShift)

    @property
    def divisor(self) -> float:
        if self.is_greek_shift:
            return list(self.curve_descriptors)[0].market_data.scenario_divisor
        raise ProgrammingError('Market data range descriptors have no divisor')

    @property
    def shift(self) -> float:
        if self.is_greek_shift:
            return list(self.curve_descriptors)[0].shift
        raise ProgrammingError('Market data range descriptors have no shift')

    @property
    def unit(self) -> str:
        if self.is_greek_shift:
            return list(self.curve_descriptors)[0].unit  # type: ignore[union-attr]
        raise ProgrammingError('Market data range descriptors have no unit')

    @property
    def scenario(self) -> str:
        return list(self.curve_descriptors)[0].scenario

    def mirror_shift(self) -> StackedCurveShift:
        return StackedCurveShift(tuple(descriptor.mirror_shift() for descriptor in self.curve_descriptors))

    def get_context(self) -> Generator[ContextManager[None], None, None]:
        for descriptor in self.curve_descriptors:
            yield from descriptor.get_context()

    def __post_init__(self) -> None:
        assert all(isinstance(descriptor, GreekShift) for descriptor in self.curve_descriptors) or all(
            isinstance(descriptor, MarketDataShift) for descriptor in
            self.curve_descriptors), 'Differing shift types in curve stack'
        if len({descriptor.scenario for descriptor in self.curve_descriptors}) != 1:
            raise DAARuntimeException('simultaneousCurveShift does not allow for different rho scenarios in curves')
        if self.is_greek_shift:
            shifts = [descriptor.shift for descriptor in self.curve_descriptors]
            if not math.isclose(max(shifts), min(shifts)):
                raise DAARuntimeException('simultaneousCurveShift does not allow for different rho shifts in curves')

    def __str__(self) -> str:
        if self.is_greek_shift:
            return ', '.join(sorted([str(descriptor) for descriptor in self.curve_descriptors]))
        scenarios_stripped = [str(descriptor).split(' ', maxsplit=1)[0] for descriptor in self.curve_descriptors]
        reference_id = ', '.join(sorted(scenarios_stripped))
        return f'{reference_id} {self.scenario}'


ShiftedPVs = OrderedDict[ShiftDescriptor, CashFlows]
GreekResults = dict[PVDescriptor, float]


class QLValuation(QLValuationBase):  # pylint: disable=abstract-method

    @property
    def instrument(self) -> QLInstrument:
        return self._instrument

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        result_types: list[str] = self.data(fields.ResultTypes, check=ContainedIn(self._allowed_greeks),
                                            allow_fallback_to_default_parameters=self._allowed_greeks == result_items.AllGreeks)
        self._instrument: QLInstrument = self.data(fields.Instrument, check=ObjectType(signatures.instrument.all))

        self._greek_shifts: dict[str, float] = {}
        for greek in result_items.AllGreeksWithShift:
            if NoValue.is_in(greek, result_types) and self._valuation_type:
                self._greek_shifts[str(greek)] = self.data(fields.GreekType(greek, self._valuation_type),
                                                           check=Range(lower=0.0),
                                                           allow_fallback_to_default_parameters=True)
        self._symmetric_greeks = self.data(fields.SymmetricGreeks, allow_fallback_to_default_parameters=True,
                                           default_value=False)
        self._simultaneous_curve_shift: bool = self.data(fields.SimultaneousCurveShift,
                                                         allow_fallback_to_default_parameters=True, default_value=False)
        self._calculate_snd_derivative: bool = self.data(fields.SecondDerivatives,
                                                         allow_fallback_to_default_parameters=True, default_value=False)
        self._significance_lower_bound: float = self.data(
            fields.GreekSignificanceLowerBound,
            check=[
                Range(lower=0.0, strict=False),
                RangeWarning(upper=1e-3)
            ],
            allow_fallback_to_default_parameters=True,
            default_value=global_parameters.GreekIsNonZero)
        self._result_types: set[str] = set(result_types + [result_items.Amount])
        self._sub_id: Optional[str] = self.data(fields.SubId, default_value=None)

    def pv_and_cashflows(self) -> CashFlows:
        raise NotImplementedError()

    def clean_dirty(self) -> CashFlows:
        raise NotImplementedError()

    def additional_info(self) -> dict[str, Any]:
        raise NotImplementedError()

    def additional_cashflow_info(self) -> list[AdditionalBondCfInfo]:
        raise NotImplementedError()

    def result_amount(self) -> None:
        try:
            currency = self._instrument.currency.id
        except Exception:  # pylint: disable=broad-except
            currency = 'Unknown'
        self._ql_db.result_db(
            ResultLineAmount(self._instrument.id, self._sub_id, self._id, self._instrument.amount, currency))
        self._result_types.discard(result_items.Amount)

    def instrument_maturity(self) -> Optional[datetime.date]:
        try:
            maturity: Optional[datetime.date] = qldate2date(
                self._instrument.maturity)  # type: ignore[attr-defined, assignment]
        except Exception:  # pylint: disable=broad-except
            try:
                maturity = qldate2date(self._instrument.maturity__d)  # type: ignore[attr-defined, assignment]
            except Exception:  # pylint: disable=broad-except
                maturity = None
        if maturity == global_parameters.DummyDate:
            maturity = None
        return maturity

    def instrument_issue(self) -> Optional[datetime.date]:
        try:
            issue: Optional[datetime.date] = qldate2date(self._instrument.issue)  # type: ignore[assignment]
        except Exception:  # pylint: disable=broad-except
            issue = None
        if issue == global_parameters.DummyDate:
            issue = None
        return issue

    def result_info(self) -> None:
        issue: Union[datetime.date, str] = self.instrument_issue() or 'Unknown'
        maturity: Union[datetime.date, str] = self.instrument_maturity() or 'Unknown'
        self._ql_db.result_db(
            ResultLineInfo(self._instrument.id, self._sub_id, self._id, issue, maturity))  # type: ignore[arg-type]
        self._result_types.discard(result_items.Info)

    def result_clean_dirty(self) -> None:
        results: CashFlows = self.clean_dirty()
        for pv_descriptor, (clean_price, dirty_price) in results.clean_and_dirty():
            self._ql_db.result_db(
                ResultLineCleanDirty(
                    self._instrument.id,
                    combine_ids(
                        self._sub_id,
                        pv_descriptor.sub_id
                    ),
                    self._id,
                    clean_price,
                    dirty_price,
                    pv_descriptor.currency.id
                )
            )
        self._result_types.discard(result_items.CleanDirty)

    def result_additional_info(self) -> None:
        additional_info: dict[str, Any] = self.additional_info()
        for key in list(additional_info):
            if isinstance(additional_info[key], CashFlows):
                del additional_info[key]
        if not additional_info:
            return
        self._ql_db.result_db(ResultLineFlexible(self._instrument.id, self._sub_id, self._id, **additional_info))
        self._result_types.discard(result_items.AdditionalInfo)

    def result_pv_and_cashflows(self) -> CashFlows:
        cash_flows = self.pv_and_cashflows()
        cash_flows.finalize_pvs(self.valuation_date)
        if result_items.PV in self._result_types:
            for pv_descriptor, amount in cash_flows.pvs(extend=True):
                self._ql_db.result_db(
                    ResultLinePV(self._instrument.id, combine_ids(self._sub_id, pv_descriptor.sub_id), self._id, amount,
                                 pv_descriptor.currency.id))
            self._result_types.discard(result_items.PV)
        if result_items.CashFlows in self._result_types:
            for cash_flow_descriptor, value, discount_factor in cash_flows.cfs(include_discount=True):
                self._ql_db.result_db(ResultLineSimpleCashFlow(self._instrument.id,
                                                               combine_ids(self._sub_id, cash_flow_descriptor.sub_id),
                                                               self._id, value, discount_factor,
                                                               cash_flow_descriptor.currency.id,
                                                               qldate2date(cash_flow_descriptor.fixing),  # type: ignore[arg-type]
                                                               qldate2date(cash_flow_descriptor.payment),  # type: ignore[arg-type]
                                                               qldate2date(cash_flow_descriptor.settlement),  # type: ignore[arg-type]
                                                               cash_flow_descriptor.cashflowtype))
            self._result_types.discard(result_items.CashFlows)
        return cash_flows

    def add_result_cashflow_info(self, cash_flows: CashFlows) -> None:
        if len(list(cash_flows.cfs())) == 0:
            additional_info: dict[str, Any] = self.additional_info()
            if not additional_info:
                return
            for key in list(additional_info):
                if isinstance(additional_info[key], CashFlows):
                    cash_flows = additional_info[key]
                    additional_cashflow_info_list: list[AdditionalBondCfInfo] = self.additional_cashflow_info()
                    self.additional_cashflow_info_helper(additional_cashflow_info_list, cash_flows)
                    del additional_info[key]
        else:
            try:
                additional_cashflow_info_list: list[AdditionalBondCfInfo] = self.additional_cashflow_info()
                self.additional_cashflow_info_helper(additional_cashflow_info_list, cash_flows)
            except NotImplementedError:
                pass

    def additional_cashflow_info_helper(self, additional_cashflow_info_list, cash_flows):
        for additional_cashflow_info, (cash_flow_descriptor, value, discount_factor) in zip(
                additional_cashflow_info_list,
                cash_flows.cfs(include_discount=True)):
            self._ql_db.result_db(ResultLineBondAdditionalInfo(self._instrument.id,
                                                               combine_ids(self._sub_id,
                                                                           cash_flow_descriptor.sub_id),
                                                               self._id, value, discount_factor,
                                                               cash_flow_descriptor.currency.id,
                                                               qldate2date(cash_flow_descriptor.fixing),  # type: ignore[arg-type]
                                                               qldate2date(cash_flow_descriptor.payment),  # type: ignore[arg-type]
                                                               qldate2date(cash_flow_descriptor.settlement),  # type: ignore[arg-type]
                                                               cash_flow_descriptor.cashflowtype,
                                                               additional_cashflow_info.leg_number,
                                                               additional_cashflow_info.start_date,
                                                               additional_cashflow_info.accrual_start,
                                                               additional_cashflow_info.accrual_end,
                                                               additional_cashflow_info.period_length,
                                                               additional_cashflow_info.period_year_frac,
                                                               additional_cashflow_info.cum_period_length,
                                                               additional_cashflow_info.notional,
                                                               additional_cashflow_info.sinking_amount,
                                                               additional_cashflow_info.rate,
                                                               additional_cashflow_info.fixed_rate,
                                                               additional_cashflow_info.forward_rate,
                                                               additional_cashflow_info.actual_coupon,
                                                               additional_cashflow_info.discounted_coupon,
                                                               additional_cashflow_info.discounted_sinking_amount,
                                                               additional_cashflow_info.risk_free_discount,
                                                               additional_cashflow_info.is_fixed))
            self._result_types.discard(result_items.CashFlows)

    def _post_init(self) -> None:
        if result_items.Amount in self._result_types:
            self.result_amount()
        if result_items.Info in self._result_types:
            self.result_info()
        if not self._result_types:
            return
        cash_flows = self.result_pv_and_cashflows()  # pylint: disable=invalid-name
        # --- Results that are only available after result_pv_and_cashflows --------------------------------------------
        if result_items.CleanDirty in self._result_types:
            self.result_clean_dirty()
        if result_items.AdditionalInfo in self._result_types:
            self.result_additional_info()
        if result_items.CashFlowsAdditionalInfo in self._result_types:
            self.add_result_cashflow_info(cash_flows)
        if result_items.MarketDataRange in self._result_types:
            up_shifts: ShiftedPVs = self._calculate_market_range()
            self._add_range_result_lines(up_shifts, cash_flows, result_items.MarketDataRange)
            self._result_types.discard(result_items.MarketDataRange)
        if self._result_types:
            up_shifts = self._calculate_greeks(cash_flows)
            if result_items.SensitivityRange in self._result_types:
                self._add_range_result_lines(up_shifts, cash_flows, result_items.SensitivityRange)

    ####################################################################################################################
    # Greeks / Ranges
    # see docs\concepts\valuation_base.md

    def _calculate_market_range(self) -> ShiftedPVs:
        result: ShiftedPVs = OrderedDict()
        market_data_references: list[Reference] = [
            market_data_or_process.reference
            for market_data_or_process in self._instrument.market_data_objects
            if isinstance(market_data_or_process, QLMarketData)
        ]

        for market_data in collect_single_or_curve_stack(market_data_references, self._ql_db,
                                                         self._simultaneous_curve_shift):
            if isinstance(market_data, tuple):
                curve_descriptors: tuple[MarketDataShift, ...] = tuple(
                    (MarketDataShift(yield_curve) for yield_curve in market_data))
                shift_descriptor: Union[MarketDataShift, StackedCurveShift] = StackedCurveShift(curve_descriptors)
            else:
                shift_descriptor = MarketDataShift(market_data)
            shifted_cash_flows = self._shift_and_recalculate_market_range(shift_descriptor)
            shifted_cash_flows.finalize_pvs(self.valuation_date)
            result[shift_descriptor] = shifted_cash_flows
        return result

    def _shift_and_recalculate_market_range(self, descriptor: Union[MarketDataShift, StackedCurveShift]) -> CashFlows:
        if isinstance(descriptor, StackedCurveShift):
            assert not descriptor.is_greek_shift
        with contextlib.ExitStack() as single_or_curve_stack:
            for context in descriptor.get_context():
                single_or_curve_stack.enter_context(context)
            scenario_cash_flows = self.pv_and_cashflows()
        return scenario_cash_flows

    def _calculate_greeks(self, base_cash_flows: CashFlows) -> ShiftedPVs:
        up_shifts: ShiftedPVs = OrderedDict()
        for greek, market_data, scenarios in self._greek_scenarios():
            greek_results_per_scenario: OrderedDict[str, CashFlows] = OrderedDict()
            second_derivatives: OrderedDict[str, CashFlows] = OrderedDict()
            compute_dv01: bool = False
            market_data_id: str = ''
            for count, scenario in enumerate(scenarios):
                if isinstance(market_data, tuple):
                    curve_descriptors: tuple[GreekShift, ...] = tuple(
                        GreekShift(yield_curve, greek, scenario, self._greek_shifts[greek]) for yield_curve in
                        market_data)
                    greek_descriptor: Union[StackedCurveShift, GreekShift] = StackedCurveShift(curve_descriptors)
                    compute_dv01 = self._symmetric_greeks or self._calculate_snd_derivative
                else:
                    greek_descriptor = GreekShift(market_data, greek, scenario, self._greek_shifts[greek])
                    compute_dv01 = market_data.signature.type == signatures.yield_curve.all.type and (self._symmetric_greeks or self._calculate_snd_derivative)
                if count == 0:
                    market_data_id = str(greek_descriptor)
                scenario_divisor, up_shifted_cash_flows = self._shift_and_re_calculate_greek(greek_descriptor)
                up_shifted_cash_flows.finalize_pvs(self.valuation_date)
                up_shifts[greek_descriptor] = up_shifted_cash_flows
                if not (self._symmetric_greeks or self._calculate_snd_derivative):
                    greek_results_per_scenario[scenario] = CashFlows.consolidate(
                        (up_shifted_cash_flows - base_cash_flows) / scenario_divisor,
                        self._significance_lower_bound
                    )
                    continue
                mirrored_descriptor: Union[GreekShift, StackedCurveShift] = greek_descriptor.mirror_shift()
                _, down_shifted_cash_flows = self._shift_and_re_calculate_greek(mirrored_descriptor)
                down_shifted_cash_flows.finalize_pvs(self.valuation_date)
                central_differences: CashFlows = CashFlows.consolidate(
                    (up_shifted_cash_flows - down_shifted_cash_flows) / (2.0 * scenario_divisor),
                    self._significance_lower_bound
                )
                greek_results_per_scenario[scenario] = central_differences
                if self._calculate_snd_derivative and greek in result_items.SndDerivatives:
                    snd_derivatives: CashFlows = CashFlows.consolidate(
                        (up_shifted_cash_flows - 2.0 * base_cash_flows + down_shifted_cash_flows) / scenario_divisor ** 2, self._significance_lower_bound)
                    second_derivatives[scenario] = snd_derivatives
                    snd_derivatives.finalize_pvs(self.valuation_date)
            self._add_greek_result_lines(base_cash_flows, greek_results_per_scenario, greek, market_data_id,
                                         compute_dv01, second_derivatives)
        return up_shifts

    def _greek_scenarios(self) -> Generator[tuple[str, Union[QLMarketData, tuple[QLMarketData, ...]], list[str]], None, None]:
        greeks: list[str] = [result_type for result_type in self._result_types if
                             result_type in result_items.AllGreeksWithShift]
        for greek in sorted(greeks):
            for single_or_curves in collect_single_or_curve_stack(self._instrument.market_data(greek), self._ql_db,
                                                                  self._simultaneous_curve_shift):
                if isinstance(single_or_curves, tuple):
                    scenarios: list[str] = list(single_or_curves)[0].scenarios(greek)
                else:
                    scenarios = single_or_curves.scenarios(greek)
                yield greek, single_or_curves, scenarios

    def _shift_and_re_calculate_greek(self, descriptor: Union[GreekShift, StackedCurveShift]) -> tuple[float, CashFlows]:
        if isinstance(descriptor, StackedCurveShift):
            assert descriptor.is_greek_shift
        with contextlib.ExitStack() as single_or_curve_stack:
            for context in descriptor.get_context():
                single_or_curve_stack.enter_context(context)
            divisor: float = descriptor.divisor
            scenario_cash_flows = self.pv_and_cashflows()
        return divisor, scenario_cash_flows

    @staticmethod
    def _make_result_line_greek(instrument_ids: tuple[str, Optional[str], str],
                                greek_name: str,
                                market_data_id: str,
                                currency: str,
                                scenarios: list[str],
                                values: list[float]) -> ResultLineGreek:
        result_args: tuple[str, Optional[str], str, str, str, str, list[str], list[float]] = instrument_ids + (
            greek_name, market_data_id, currency) + (scenarios, values)
        return ResultLineGreek(*result_args)

    def _add_greek_result_lines(self, base_cash_flows: CashFlows,
                                greeks_per_scenario: OrderedDict[str, CashFlows],
                                greek: str,
                                market_data_id: str,
                                compute_dv01: bool,
                                second_derivatives: OrderedDict[str, CashFlows]) -> None:
        # TODO(22/06): We could add the "unit/convention" (e.g "pct", "bps") to ResultLineGreek
        for pv_descriptor, _ in base_cash_flows.pvs():
            sub_id = combine_ids(self._sub_id, pv_descriptor.sub_id)
            instrument_ids: tuple[str, Optional[str], str] = (self._instrument.id, sub_id, self.id)
            headers: list[str] = []
            snd_dev_headers: list[str] = []
            # TODO(22/07) Remove when scenarios have been improved
            snd_scenario_map: dict[str, str] = {
                result_items.Delta: result_items.Gamma,
                result_items.Vega: result_items.Volga,
                result_items.Rho: result_items.DRho
            }
            values: list[float] = []
            snd_dev_values: list[float] = []
            for scenario, scenario_greeks in greeks_per_scenario.items():
                headers.append(scenario)
                values.append(scenario_greeks[pv_descriptor])
                if second_derivatives:
                    snd_dev_headers.append(snd_scenario_map.get(scenario, scenario))
                    snd_dev_values.append(second_derivatives[scenario][pv_descriptor])
            currency = pv_descriptor.currency.id
            self.ql_db.result_db(
                self._make_result_line_greek(
                    instrument_ids,
                    greek,
                    market_data_id,
                    currency,
                    headers,
                    values
                )
            )
            if snd_dev_values:
                scd_dev_name = result_items.SndDerivatives[greek]
                self.ql_db.result_db(
                    self._make_result_line_greek(
                        instrument_ids,
                        scd_dev_name,
                        market_data_id,
                        currency,
                        snd_dev_headers,
                        snd_dev_values
                    )
                )
            if compute_dv01:
                # docs/formulas/DV01_BBG.PNG
                dv01 = -sum(values)
                self.ql_db.result_db(
                    self._make_result_line_greek(
                        instrument_ids,
                        result_items.DV01,
                        market_data_id,
                        currency,
                        [result_items.DV01],
                        [dv01]
                    )
                )
                if snd_dev_values:
                    dv01_gamma = -sum(snd_dev_values)
                    self.ql_db.result_db(
                        self._make_result_line_greek(
                            instrument_ids,
                            result_items.SndDerivatives[result_items.DV01],
                            market_data_id,
                            currency,
                            [result_items.SndDerivatives[result_items.DV01]],
                            [dv01_gamma]
                        )
                    )

    # Refine if stationary npv points become a problem
    def _add_range_result_lines(self, up_shifts: ShiftedPVs, cash_flows: CashFlows, range_result_type: str) -> None:
        up_descriptors: list[ShiftDescriptor] = []
        for shift_descriptor, up_pvs in up_shifts.items():
            difference: float = (up_pvs - cash_flows).sum_pvs()
            if range_result_type == result_items.MarketDataRange:
                lower_bound = global_parameters.MarketDataRangeIsNonZero
            else:
                lower_bound = abs(shift_descriptor.shift) * self._significance_lower_bound
            if abs(difference) > lower_bound:
                if difference > 0:
                    up_descriptors.append(shift_descriptor)
                else:
                    up_descriptors.append(shift_descriptor.mirror_shift())
        down_descriptors: list[ShiftDescriptor] = [item.mirror_shift() for item in up_descriptors]
        if range_result_type == result_items.MarketDataRange:
            high_info = '|'.join(sorted([str(item) for item in up_descriptors]))
            low_info = '|'.join(sorted([str(item) for item in down_descriptors]))
        else:
            high_info = '|'.join(sorted([f'{item} {item.scenario} {item.shift}{item.unit}' for item in
                                         up_descriptors]))  # type: ignore[attr-defined]
            low_info = '|'.join(sorted([f'{item} {item.scenario} {item.shift}{item.unit}' for item in
                                        down_descriptors]))  # type: ignore[attr-defined]

        high_cash_flows = self._shift_and_re_calculate_stacked(up_descriptors)
        low_cash_flows = self._shift_and_re_calculate_stacked(down_descriptors)
        range_type = range_result_type.replace('Range', '')

        for pv_descriptor, high_pv in high_cash_flows.pvs():
            sub_id = combine_ids(self._sub_id, pv_descriptor.sub_id)
            currency = pv_descriptor.currency.id
            result_line = ResultLineRange(self._instrument.id, sub_id, self.id, currency, range_type, high_info,
                                          high_pv, low_info, low_cash_flows[pv_descriptor])
            self.ql_db.result_db(result_line)

    def _shift_and_re_calculate_stacked(self, descriptors: Iterable[ShiftDescriptor]) -> CashFlows:
        with contextlib.ExitStack() as market_data_stack:
            for descriptor in descriptors:
                for context in descriptor.get_context():
                    market_data_stack.enter_context(context)
            scenario_cash_flows = self.pv_and_cashflows()
            scenario_cash_flows.finalize_pvs(self.valuation_date)
        return scenario_cash_flows


class QLValuationInfo(QLValuation):  # pylint: disable=abstract-method
    _signature = signatures.valuation.simple
    _valuation_type = None
    _allowed_greeks = [result_items.Amount, result_items.Info]


@singledispatch
def get_currency_and_subtype(_: Union[Reference, tuple[Reference, str]]) -> tuple[Reference, Optional[str]]:
    raise ProgrammingError('Parameter hat to be either Reference or tuple[Reference, str]')


@get_currency_and_subtype.register(Reference)
def _(currency_and_subtype: Reference) -> tuple[Reference, None]:
    return currency_and_subtype, None


@get_currency_and_subtype.register(tuple)  # type: ignore[no-redef]
def _(currency_and_subtype: tuple[Reference, str]) -> tuple[Reference, str]:
    assert isinstance(currency_and_subtype[0], Reference)
    assert isinstance(currency_and_subtype[1], str)
    return currency_and_subtype


# Todo 2021/01  This class seems to be a bit odd; at least its name and its purpose do not seem to coincide! Just move it to QLImpliedZSpread ???
class QLValuationHelper(QLValuationBase):
    _admissible_instrument_types: list[Signature] = []

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._instrument: QLInstrument = self.data(fields.Instrument,
                                                   check=ObjectType(self._admissible_instrument_types))

        self._sub_id = self.data(fields.SubId, default_value=None)

    def result_z_spread(self) -> float:
        raise NotImplementedError()
