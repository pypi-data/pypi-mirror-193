from __future__ import annotations

from valuation.consts import signatures
from valuation.consts import fields
from valuation.engine.check import ObjectType
from valuation.engine.market_data import QLMarketData
from valuation.engine.utils import qldate2date
from valuation.engine.valuation import QLValuationBase
from valuation.global_settings import __type_checking__
from valuation.universal_output import ResultLineMarketData

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage


class QLValuationMarketData(QLValuationBase):
    _signature = signatures.valuation.market_data

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._fixing_date = self.data(fields.FixingDate)
        self._market_data: QLMarketData = self.data(fields.MarketData, check=ObjectType([signatures.fx_rate.all, signatures.yield_curve.all, signatures.ir_index.all]))
        self._optional_info: str = self.data(fields.OptionalInfo, default_value='')

    def _post_init(self) -> None:
        result_line: ResultLineMarketData = ResultLineMarketData(self.id, str(self._market_data.reference), qldate2date(self._fixing_date), self._market_data.evaluate(self._fixing_date, self._optional_info))
        self._ql_db.result_db(result_line)
