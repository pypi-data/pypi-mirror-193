from __future__ import annotations

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.utils import period2qlfrequency
from valuation.engine.valuation import QLValuationHelper
from valuation.universal_output import ResultLineImpliedZSpread

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage


class QLImpliedZSpreadValuation(QLValuationHelper):  # pylint: disable=abstract-method
    _signature = signatures.valuation.implied_zspread
    _valuation_type = None
    _admissible_instrument_types = [signatures.instrument.fixed_bond, signatures.instrument.float_bond]

    # Todo: (2020/12)
    #       add a flag for multiple legs, only work if we work with single legs
    #       FB:
    #       At least add an assertion.

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._z_price: float = self.data(fields.ZSpreadPrice)
        self._z_settlement_date: ql.Date = self.data(fields.ZSpreadSettlementDate, default_value=self.valuation_date)
        self._z_accuracy: float = self.data(fields.ZSpreadAccuracy, default_value=1.0e-10)
        self._z_max_iter: int = self.data(fields.ZSpreadMaxIter, default_value=100)
        self._z_guess: float = self.data(fields.ZSpreadGuess, default_value=0.0)

    def result_z_spread(self) -> float:
        return self.z_spread_evaluate(self._z_price * 100, self._z_settlement_date, self._z_accuracy, self._z_max_iter,
                                      self._z_guess)

    def z_spread_evaluate(self,
                          external_price: float,
                          settlement_date: ql.Date,
                          accuracy: float,
                          max_iter: int,
                          guess: float) -> float:
        unique_dates: set[ql.Date] = {cf.date()
                                      for cf in self._instrument.instrument.cashflows()
                                      if cf.date() >= settlement_date}
        unique_dates.add(
            max(unique_dates) + 7)  # Add a week, somehow zSpread calculation needs some extra time after maturity
        unique_dates.add(settlement_date)

        new_dates: list[ql.Date] = sorted(unique_dates)
        discount_curve = self._instrument.discount_curve.get_discount_curve_risk_free(new_dates)
        frequency = period2qlfrequency(self._instrument.schedule.tenor)  # type: ignore[attr-defined]
        # SWIGs\bondfunctions.i
        #   BondFunctions.zSpread --> float
        #       bond    Bond
        #       cleanPrice  Real
        #       discountCurve   YieldTermStructure
        #       dayCounter  DayCounter
        #       compounding Compounding
        #       frequency   Frequency
        #       settlementDate  Date    (Date())
        #       accuracy    Real    (1.0e-10)
        #       maxIterations   Size    (100)
        #       guess   Rate    (0.0)
        # Todo: (2020/12)
        #       could expand this to allow for simple/continuous
        #       FB:
        #       Please follow the ideas used in other cases, i.e.
        #       *   giving a sensible default value (i.e. ql.Compounded)
        #       *   Use mappings.Compounding
        return ql.BondFunctions.zSpread(self._instrument.instrument,  # type: ignore[no-any-return]
                                        external_price,
                                        discount_curve,
                                        self._instrument.daycount,
                                        ql.Compounded,
                                        frequency,
                                        settlement_date,
                                        accuracy,
                                        max_iter,
                                        guess
                                        )

    def _post_init(self) -> None:
        z_spread: float = self.result_z_spread()
        self._ql_db.result_db(ResultLineImpliedZSpread(self._instrument.id,
                                                       self._sub_id,
                                                       self._id,
                                                       z_spread))
