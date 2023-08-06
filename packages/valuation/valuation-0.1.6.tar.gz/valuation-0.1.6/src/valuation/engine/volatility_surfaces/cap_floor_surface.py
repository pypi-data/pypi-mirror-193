from __future__ import annotations
import QuantLib as ql

from valuation.global_settings import __type_checking__
from valuation.consts import signatures, types, global_parameters
from valuation.consts import fields
from valuation.engine import QLObject
from valuation.engine import defaults
from valuation.engine.check import IsOrdered, Range
from valuation.engine.utils import period2qlperiod
from valuation.engine.mappings import VolatilityType
from valuation.engine.volatility_surfaces.base_object import QLVolatility
from valuation.universal_transfer import Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.mappings import QLBusiness, QLVolatilityType
    from valuation.engine.market_data import QLCurrency
    from valuation.universal_transfer import DefaultParameters, Storage


class QLCapFloorVolatility(QLVolatility):
    _signature = signatures.cap_floor_surface

    @property  # type: ignore[misc]
    @QLObject.moves_to_shifted
    def ql_surface(self) -> ql.CapFloorTermVolSurface:
        return self._ql_surface

    def __init__(self,
                 data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters = None,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode=data_only_mode)

        self._currency: QLCurrency = self.data(fields.Currency)
        self._expiries, self._strikes, self._vol_surface = self.data_matrix(fields.Surface,
                                                                            row_type=types.Periods,
                                                                            col_type=types.Floats,
                                                                            content_type=types.FloatMatrix,
                                                                            row_check=IsOrdered(),
                                                                            col_check=IsOrdered(),
                                                                            content_check=Range(lower=0.0,
                                                                                                upper=global_parameters.VolatilityMaximum))
        self._daycount: ql.DayCounter = self.data(fields.DayCount, default_value=defaults.daycount(self._currency.id))
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.id)
        self._business: QLBusiness = self.data(fields.Business, default_value=defaults.business(self._currency.id))
        self._distribution: QLVolatilityType = self.data(fields.Distribution, ql_map=VolatilityType)
        self._settlement_days: int = self.data(fields.SettlementDays, default_value=defaults.settlement_days(self._currency.id, Period(3, 'M')),
                                               check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum,
                                                           strict=False))

        self._ql_surface: ql.CapFloorTermVolSurface

    def _post_init(self) -> None:
        # SWIGs\old_volatility.i
        # 	CapFloorTermVolSurface
        # 		settlementDays	Natural
        # 		calendar	Calendar
        # 		bdc	BusinessDayConvention
        # 		optionTenors	vector<Period>
        # 		strikes	vector<Rate>
        # 		quotes	vector< vector<Handle<Quote> > >
        # 		dc	DayCounter		(QuantLib::Actual365Fixed ( ))
        ql_expiries = period2qlperiod(self._expiries)
        self._ql_surface = ql.CapFloorTermVolSurface(
            self._settlement_days,
            self._calendar,
            self._business,
            ql_expiries,
            self._strikes,
            ql.Matrix(self._vol_surface),
            self._daycount
        )
