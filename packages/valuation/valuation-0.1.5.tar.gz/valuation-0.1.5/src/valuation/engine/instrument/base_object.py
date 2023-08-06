from __future__ import annotations

import math
from collections import defaultdict
from copy import deepcopy
from typing import Any, Callable, Optional, Union

import QuantLib as ql

from valuation.consts import signatures, global_parameters
from valuation.consts import fields
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine import QLObject
from valuation.engine.check import Check, Equals, ObjectType, Range
from valuation.engine.exceptions import QLInputError, UnsupportedValuationError
from valuation.engine.instrument.payoff_language import PL_CashFlows, StackValue, Statement, evaluate_statements, \
    financial_program_to_statements
from valuation.engine.mappings import AugmentedDict
from valuation.engine.process import QLProcess, generate_dummy_process
from valuation.engine.utils import CashFlowDescriptor, PVDescriptor, CashFlows
from valuation.universal_transfer import DefaultParameters, NoValue, Storage, StorageTypes
from valuation.utils.other import Timer

if __debug__:
    import inspect

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import TypeKey, Signature
    from valuation.engine import QLObjectDB, QuantlibType
    from valuation.engine.instrument.coupons.base_object import QLCoupon
    from valuation.engine.market_data import QLCurrency, QLMarketData, QLYieldCurve
    from valuation.engine.process.path import Path


class QLInstrument(QLObject):  # pylint: disable=abstract-method, too-many-public-methods
    _pay_off: str = ''
    _market_data_name: Optional[TypeKey] = None
    _market_data_types: list[Signature] = []

    @property
    def instrument(self) -> ql.Instrument:
        return self._instrument

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def currency(self) -> QLCurrency:
        try:
            return self._currency
        except AttributeError:
            self._currency: QLCurrency = self._discount_curve.currency
            return self._currency

    @property
    def issue(self) -> ql.Date:
        return self._issue

    @property
    def maturity(self) -> ql.Date:
        if not self._maturity:
            raise QLInputError('Missing maturity')
        return self._maturity

    @property
    def pay_off(self) -> Optional[str]:
        return self._pay_off

    @property
    def process(self) -> QLProcess:
        return self._process

    @property
    def daycount(self) -> ql.DayCounter:
        return self._daycount

    @property
    def discount_curve(self) -> QLYieldCurve:
        return self._discount_curve

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._continuous_period: Optional[tuple[ql.Date, ql.Date]] = None  # Should be overwritten, if appropriate!
        self._amount: float = self.data(fields.Amount, default_value=1.0)
        self._is_alive: bool = self.data(fields.IsAlive, default_value=True)
        self._issue: ql.Date = self.data(fields.Issue, default_value=global_parameters.DummyDate)
        self._maturity: ql.Date = self.data(fields.Maturity, default_value=global_parameters.DummyDate,
                                            check=Range(lower=self._issue, strict=False))
        self._process: QLProcess = self.data(fields.StochasticProcess, default_value=None,
                                             check=ObjectType(signatures.process.all))

        if self._market_data_name is not None:
            if self._process is None:
                self._market_data_of_process: QLMarketData = self.data(self._market_data_name,
                                                                       check=ObjectType(self._market_data_types))
                self._process = generate_dummy_process(self._market_data_of_process)
            else:
                attached_market_data = self._process.attached_market_data
                attached_market_data = NoValue.replace(attached_market_data, 'attached_market_data',
                                                       self._market_data_name)
                self._market_data_of_process = self.data(self._market_data_name, default_value=attached_market_data,
                                                         check=[Equals(attached_market_data),
                                                                ObjectType(self._market_data_types)])
        elif self._process is not None:
            self._market_data_of_process = self._process.attached_market_data
            if self._market_data_of_process.supported_greeks:
                self._market_data_objects.add(self._market_data_of_process)
        else:
            self._market_data_of_process = None
            self._process = generate_dummy_process(self)

        self._variables: dict[str, StackValue]
        self._variables_permanent: dict[str, StackValue]
        self._cash_flows: PL_CashFlows
        self._cash_flows_continuous: PL_CashFlows
        self._currency: QLCurrency  # type: ignore[no-redef]
        self._discount_curve: QLYieldCurve
        self._instrument: ql.Instrument
        self._daycount: ql.DayCounter

    def data(self, type_key: TypeKey,
             default_value: Union[QLObject, StorageTypes.GeneralEntry, NoValue, None] = NoValue(),
             check: Union[None, Check, list[Check]] = None, allow_fallback_to_default_parameters: bool = False,
             ql_map: Optional[AugmentedDict[QuantlibType, QuantlibType]] = None,
             ignore_data_only_mode: bool = False, exclude_from_greeks: bool = False) -> QuantlibType:
        value = super().data(type_key, default_value, check, allow_fallback_to_default_parameters, ql_map,
                             ignore_data_only_mode, exclude_from_greeks)
        if isinstance(value, QLObject) and exclude_from_greeks and value.supported_greeks:
            self._market_data_objects.add(value)
        return value

    def _financial_program_evaluate_single_path(self, path: Path, specific_statements: dict[ql.Date, list[Statement]],
                                                continuous_statements: list[Statement], compute_all: bool,
                                                tolerance_for_equality: Optional[float]) -> None:
        for observation, date in path.observations():
            self._variables['__last_alive'] = self._variables['__alive']
            if date != global_parameters.DummyDate:
                if date <= self._valuation_date:
                    tolerance_for_equality_used: Optional[float] = 0.0
                else:
                    tolerance_for_equality_used = tolerance_for_equality
                evaluate_statements(specific_statements[date], self._variables, path, observation, self._cash_flows,
                                    tolerance_for_equality_used)
            if observation in path.continuous_mask and (compute_all or path.continuous_mask[observation]):
                evaluate_statements(continuous_statements, self._variables, path, observation,
                                    self._cash_flows_continuous, tolerance_for_equality)

    @staticmethod
    def _consolidate_cash_flows(log_number_of_paths: int, cash_flows_raw: PL_CashFlows) -> CashFlows:

        cash_flows: CashFlows = CashFlows(allows_undiscounted_cashflows=False)

        result: dict[CashFlowDescriptor, float] = defaultdict(float)
        for cash_flow_descriptor in cash_flows_raw:
            for entry in cash_flows_raw[cash_flow_descriptor]:
                result[cash_flow_descriptor] += entry
        if __debug__:
            for cash_flow_descriptor in result:
                if cash_flow_descriptor.payment > cash_flow_descriptor.settlement:
                    raise ProgrammingError(
                        f'It needs to hold {cash_flow_descriptor.fixing} <= {cash_flow_descriptor.payment} <= {cash_flow_descriptor.settlement}')
        for cash_flow_descriptor, amount in result.items():
            cash_flows.add(cash_flow_descriptor, amount / 2 ** log_number_of_paths)

        return cash_flows

    @staticmethod
    def _consolidate_cash_flows_continuous(log_number_of_paths: int, cash_flows_raw: PL_CashFlows) -> CashFlows:
        cash_flows: CashFlows = CashFlows(allows_undiscounted_cashflows=False)
        result: dict[PVDescriptor, float] = defaultdict(float)
        for cash_flow_descriptor in cash_flows_raw:
            for entry in cash_flows_raw[cash_flow_descriptor]:
                result[cash_flow_descriptor.pv_descriptor] += entry
        for pv_descriptor, amount in result.items():
            cash_flows.add_continuous_pv(pv_descriptor, amount / 2 ** log_number_of_paths)
        return cash_flows

    def _financial_program_evaluate_all_paths(self, simulation_times: list[float], observation_mask: dict[int, ql.Date],
                                              continuous_mask: dict[int, bool], log_number_of_paths: int,
                                              generator_type: str, brownian_bridge: bool, antithetic: bool,
                                              tolerance_for_equality: Optional[float],
                                              specific_statements: dict[ql.Date, list[Statement]],
                                              continuous_statements: list[Statement],
                                              non_observation_dates: dict[ql.Date, float],
                                              simulation_time_map: dict[int, float], compute_all: bool) -> CashFlows:
        self._variables_permanent = {'__alive': self._is_alive}
        self._cash_flows = defaultdict(list)
        self._cash_flows_continuous = defaultdict(list)
        with Timer(f'MC: {self.signature}\t{self.reference}\tlog(#): {log_number_of_paths}', log_total_time=True,
                   shadow_timer=True):
            for path in self._process.paths(simulation_times, observation_mask, continuous_mask, non_observation_dates,
                                            simulation_time_map, log_number_of_paths, generator_type, brownian_bridge,
                                            antithetic):
                self._variables = deepcopy(self._variables_permanent)
                self._financial_program_evaluate_single_path(path, specific_statements, continuous_statements,
                                                             compute_all, tolerance_for_equality)
        if len(simulation_times) == 1:
            cash_flows = self._consolidate_cash_flows(0, self._cash_flows)
            cash_flows_continuous = self._consolidate_cash_flows_continuous(0, self._cash_flows_continuous)
        else:
            cash_flows = self._consolidate_cash_flows(log_number_of_paths, self._cash_flows)
            cash_flows_continuous = self._consolidate_cash_flows_continuous(log_number_of_paths,
                                                                            self._cash_flows_continuous)

        return cash_flows + cash_flows_continuous

    def _financial_program_evaluate(self, maximal_time_stepping_in_days: float,
                                    continuous_time_stepping_in_days: Optional[float], log_number_of_paths: int,
                                    generator_type: str, brownian_bridge: bool, antithetic: bool,
                                    tolerance_for_equality: Optional[float], enable_broadie_glassermann: bool,
                                    pay_off_override: Optional[str] = None,
                                    base_object: Optional[Union[QLInstrument, list[QLCoupon]]] = None) -> CashFlows:
        pay_off: str = pay_off_override or self._pay_off
        base_object = base_object or self

        if not pay_off:
            raise UnsupportedValuationError(signatures.valuation.financial_program, self.signature)

        specific_statements, continuous_statements, observation_dates, non_observation_dates = financial_program_to_statements(
            pay_off, base_object)
        simulation_times, observation_mask, continuous_mask, non_observation_dates_augmented, simulation_time_map = self._market_data_of_process.generate_simulation_year_fractions(
            observation_dates, non_observation_dates, maximal_time_stepping_in_days, self._continuous_period,
            continuous_time_stepping_in_days)

        cash_flows = self._financial_program_evaluate_all_paths(simulation_times, observation_mask, continuous_mask,
                                                                log_number_of_paths, generator_type, brownian_bridge,
                                                                antithetic, tolerance_for_equality, specific_statements,
                                                                continuous_statements, non_observation_dates_augmented,
                                                                simulation_time_map, True)
        # cf. M. Broadie, P. Glassermann, S. Kou; A Continuity Correction for Discrete Barrier Options; Mathematical Finance, Vol 7, N. 4; 1997; pp.  325-348
        # https://www0.gsb.columbia.edu/faculty/pglasserman/Other/bgk_mf.pdf
        # The extrapolation formula gained by combination of
        # * rearranging the taylor expansion.
        # * exactly doubling the observation points which allows for removal of the Riemann-Zeta function
        if continuous_statements and enable_broadie_glassermann:
            cash_flows_coarse = self._financial_program_evaluate_all_paths(simulation_times, observation_mask,
                                                                           continuous_mask, log_number_of_paths,
                                                                           generator_type, brownian_bridge, antithetic,
                                                                           tolerance_for_equality, specific_statements,
                                                                           continuous_statements,
                                                                           non_observation_dates_augmented,
                                                                           simulation_time_map, False)
            cash_flows = (cash_flows - math.sqrt(0.5) * cash_flows_coarse) / (1.0 - math.sqrt(0.5))
        return cash_flows

    def financial_program_evaluate(self, maximal_time_stepping_in_days: float,
                                   continuous_time_stepping_in_days: Optional[float], log_number_of_paths: int,
                                   generator_type: str, brownian_bridge: bool, antithetic: bool,
                                   tolerance_for_equality: Optional[float],
                                   enable_broadie_glassermann: bool) -> CashFlows:
        return self._financial_program_evaluate(maximal_time_stepping_in_days, continuous_time_stepping_in_days,
                                                log_number_of_paths, generator_type, brownian_bridge, antithetic,
                                                tolerance_for_equality, enable_broadie_glassermann)

    def analytic_evaluate(self) -> CashFlows:
        raise UnsupportedValuationError(signatures.valuation.analytic, self.signature)

    def analytic_ql_evaluate(self) -> CashFlows:
        raise UnsupportedValuationError(signatures.valuation.analytic_quantlib, self.signature)

    def monte_carlo_evaluate(self) -> CashFlows:
        raise UnsupportedValuationError(Signature('Valuation', 'MonteCarlo'), self.signature)

    def grid_evaluate(self) -> CashFlows:
        raise UnsupportedValuationError(Signature('Valuation', 'Grid'), self.signature)

    def tree_ql_evaluate(self, maximal_time_stepping_in_days: int) -> CashFlows:
        raise UnsupportedValuationError(signatures.valuation.tree_quantlib, self.signature)

    def ql_clean_dirty(self) -> CashFlows:
        raise NotImplementedError

    def ql_additional_info(self) -> dict[str, Any]:
        raise NotImplementedError

    def additional_info(self) -> dict[str, Any]:
        raise NotImplementedError

    def ql_additional_cashflow_info(self):
        raise NotImplementedError

    def safe_call(self, ql_function: Callable[[], float], past_exception: str = '') -> float:
        if not __debug__:
            return ql_function()
        try:
            return ql_function()
        except RuntimeError as exception:
            if str(exception) == past_exception:
                raise exception
            if 'Missing' in str(exception) and ' fixing for ' in str(exception):
                _, exception_date_str = str(exception).split(' for ')
                exception_date_str = exception_date_str.replace('th,', '').replace('st,', '').replace('nd,',
                                                                                                      '').replace('rd,',
                                                                                                                  '')
                month, day, year = exception_date_str.split(' ')
                if len(day) < 2:
                    day = f'0{day}'
                final_exc_str = f'{month} {day} {year}'
                exception_date = ql.DateParser_parseFormatted(final_exc_str, '%B %d %Y')
                try:
                    self._market_data_of_process[exception_date]
                except TypeError as error:  # self._market_data_of_process may be None
                    index, _ = str(exception).split('_', 1)
                    index = index.replace('Missing ', '')
                    raise RuntimeError(
                        f'market_data_of_process is None, missing {index} fixing for {exception_date}') from error

                return self.safe_call(ql_function, str(exception))
            raise exception
        except Exception as exception:
            raise exception

    @classmethod
    def supported_valuations(cls) -> list[str]:
        valuations: list[str] = []
        if UnsupportedValuationError.__name__ not in inspect.getsource(cls.analytic_evaluate):
            valuations.append('Analytic')
        if UnsupportedValuationError.__name__ not in inspect.getsource(cls.analytic_ql_evaluate):
            valuations.append('AnalyticQuantlib')
        if cls._pay_off or cls.signature == signatures.instrument.flexible_montecarlo:  # pylint: disable=comparison-with-callable
            valuations.append('FinancialProgram')
        if UnsupportedValuationError.__name__ not in inspect.getsource(cls.grid_evaluate):
            valuations.append('Grid')
        if UnsupportedValuationError.__name__ not in inspect.getsource(cls.monte_carlo_evaluate):
            valuations.append('MonteCarlo')
        if UnsupportedValuationError.__name__ not in inspect.getsource(cls.tree_ql_evaluate):
            valuations.append('TreeQuantlib')
        return valuations

    if __debug__:
        def available_valuations(self) -> list[str]:
            valuations = self.supported_valuations().copy()
            if self._process.sub_type == '' and 'FinancialProgram' in valuations:
                valuations.pop(valuations.index('FinancialProgram'))
            return valuations
