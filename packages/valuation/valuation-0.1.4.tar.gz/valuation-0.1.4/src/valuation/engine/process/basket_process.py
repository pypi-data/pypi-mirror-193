from __future__ import annotations

from typing import Callable, Union

import QuantLib as ql

from valuation.consts import signatures, types
from valuation.consts import fields
from valuation.consts.pl import PathAll, PathSeparatedValue, PathValue
from valuation.global_settings import __type_checking__
from valuation.engine.check import MatrixDiagIsOne, MatrixHasPositiveEigenValues, MatrixIsSymmetric, ObjectType, Range
from valuation.engine.exceptions import QLInputError
from valuation.engine.market_data import QLMarketData
from valuation.engine.process import QLProcess
from valuation.engine.process.path import PathDescriptor, QLPathGenerator, path_generator_factory
from valuation.universal_transfer import DefaultParameters, STORAGE_ID_SEPARATOR, Storage

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.utils import StockDividends
    from valuation.engine.market_data import QLMarketDataBasket


class QLBasketProcess(QLProcess):                             # pylint: disable=abstract-method
    _signature = signatures.process.basket
    _initializes_past = False

    def __getitem__(self, date: ql.Date) -> dict[str, float]:                                    # type: ignore[override]
        return self._attached_market_data[date]                                                  # type: ignore[no-any-return]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super(QLProcess, self).__init__(data, ql_db, default_parameters, data_only_mode)            # pylint: disable=bad-super-call

        self._sub_processes, _, self._correlation = self.data_matrix(fields.Correlation,
                                                                     row_type=types.References,
                                                                     col_type=types.References,
                                                                     content_type=types.FloatMatrix,
                                                                     content_check=Range(lower=-1.0, upper=1.0, strict=False),
                                                                     matrix_check=[MatrixDiagIsOne(), MatrixIsSymmetric(), MatrixHasPositiveEigenValues()])
        self._attached_market_data = self.data(fields.MarketData, default_value=None, check=ObjectType(signatures.market_data_basket))

        if not self._documentation_mode:
            process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = [path_generator_factory]
            assignments: dict[Union[int, tuple[int, int]], str] = {}
            aliases: dict[str, str] = {PathAll: PathAll + PathSeparatedValue,
                                       PathValue: PathAll + PathSeparatedValue}
            allow_discount: set[str] = set()
            stock_modifier: dict[str, StockDividends] = {}
            for counter, sub_process in enumerate(self._sub_processes):
                sub_descriptor: PathDescriptor = sub_process._descriptor
                if len(sub_descriptor.process2generator_factories) != 1:
                    raise QLInputError('Just simple processes allowed for basket')
                if len(sub_descriptor.assignments) != 1:
                    raise QLInputError('Just 1D processes allowed for correlated basket; switch to non-correlated instead!')
                assignments[(0, counter)] = sub_descriptor.assignments[0]
                for key, value in sub_descriptor.aliases.items():
                    if value.startswith(key):
                        aliases[key] = value
                allow_discount.update(sub_descriptor.allow_discount)
                stock_modifier |= sub_descriptor.stock_modifier
                summations: dict[str, set[str]] = {}
            self._descriptor = PathDescriptor(process2generator_factories, assignments, aliases, allow_discount, stock_modifier, summations)

    def _post_init(self) -> None:
        if not self._attached_market_data:
            attached_market_data: list[QLMarketData] = [sub_process.attached_market_data for sub_process in self._sub_processes]
            self._market_data_names: list[str] = [market_data.id for market_data in attached_market_data]  # pylint: disable=attribute-defined-outside-init

            dummy_market_data = Storage()
            dummy_market_data[fields.Type] = 'MarketData'
            dummy_market_data[fields.SubType('MarketData')] = 'Basket'
            dummy_market_data[fields.MarketDataBasket] = tuple(md.reference for md in attached_market_data)
            dummy_market_data.make_immutable()
            dummy_market_data.assign_post_mutable_id(self.id + STORAGE_ID_SEPARATOR + 'DUMMY')

            if dummy_market_data.reference not in self.ql_db.storage_db:  # type: ignore[operator]
                self.ql_db.storage_db.add(dummy_market_data)  # type: ignore[union-attr]
            self._attached_market_data = self.ql_db[dummy_market_data.reference]

        for sub_process in self._sub_processes:
            self._market_data_objects.add(sub_process)
        if __debug__:
            for sub_market_data, process in zip(self._attached_market_data.sub_market_data, self._sub_processes):
                if sub_market_data.reference != process.attached_market_data.reference:
                    raise QLInputError('Market data in the MarketDataBasket and ProcessBasket have to be equal and in same order!')

    def _generate_process(self) -> ql.StochasticProcess:
        processes: list[ql.StochasticProcess] = [sub_process._generate_process() for sub_process in self._sub_processes]        # pylint: disable=protected-access  # Friends of QLBasketProcess
        return ql.StochasticProcessArray(processes, self._correlation)


class QLUncorrelatedBasketProcess(QLProcess):                             # pylint: disable=abstract-method
    _signature = signatures.process.uncorrelated_basket
    _initializes_past = False

    def __getitem__(self, date: ql.Date) -> dict[str, float]:                                    # type: ignore[override]
        return self._attached_market_data[date]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super(QLProcess, self).__init__(data, ql_db, default_parameters, data_only_mode)            # pylint: disable=bad-super-call

        self._sub_processes: list[QLProcess] = self.data(fields.StochasticProcesses, check=ObjectType(signatures.process.all))
        self._attached_market_data: QLMarketDataBasket = self.data(fields.MarketData, default_value=None, check=ObjectType(signatures.market_data_basket))

        if not self._documentation_mode:
            process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = []
            assignments: dict[Union[int, tuple[int, int]], str] = {}
            aliases: dict[str, str] = {PathAll: PathAll + PathSeparatedValue,
                                       PathValue: PathAll + PathSeparatedValue}
            allow_discount: set[str] = set()
            stock_modifier: dict[str, StockDividends] = {}
            for counter, sub_process in enumerate(self._sub_processes):
                sub_descriptor: PathDescriptor = sub_process._descriptor
                if len(sub_descriptor.process2generator_factories) != 1:
                    raise QLInputError('Just simple processes allowed for basket')
                process2generator_factories.append(sub_descriptor._process2generator_factories[0])
                if len(sub_descriptor.assignments) == 1:
                    assignments[counter] = sub_descriptor._assignments[0]
                else:
                    for sub_counter in sub_descriptor.assignments:
                        if sub_counter[0] != 0:         # type: ignore[index]
                            raise QLInputError('Just simple processes allowed for basket')
                        assignments[(counter, sub_counter[1])] = sub_descriptor._assignments[sub_counter]       # type: ignore[index]
                for key, value in sub_descriptor.aliases.items():
                    if value.startswith(key):
                        aliases[key] = value
                allow_discount.update(sub_descriptor.allow_discount)
                stock_modifier |= sub_descriptor.stock_modifier
                summations: dict[str, set[str]] = {}
            self._descriptor = PathDescriptor(process2generator_factories, assignments, aliases, allow_discount, stock_modifier, summations)

    def _post_init(self) -> None:
        if not self._attached_market_data:
            attached_market_data: list[QLMarketData] = [sub_process.attached_market_data for sub_process in self._sub_processes]
            self._market_data_names: list[str] = [attached_market_data.id for attached_market_data in attached_market_data]

            dummy_market_data = Storage()
            dummy_market_data[fields.Type] = 'MarketData'
            dummy_market_data[fields.SubType('MarketData')] = 'Basket'
            dummy_market_data[fields.MarketDataBasket] = tuple(md.reference for md in attached_market_data)
            dummy_market_data.make_immutable()
            dummy_market_data.assign_post_mutable_id(self.id + STORAGE_ID_SEPARATOR + 'DUMMY')

            if dummy_market_data.reference not in self.ql_db.storage_db:  # type: ignore[operator]
                self.ql_db.storage_db.add(dummy_market_data)  # type: ignore[union-attr]
            self._attached_market_data = self.ql_db[dummy_market_data.reference]  # type: ignore[assignment]
        for sub_process in self._sub_processes:
            self._market_data_objects.add(sub_process)
        if __debug__:
            for sub_market_data, process in zip(self._attached_market_data.sub_market_data, self._sub_processes):
                if sub_market_data.reference != process.attached_market_data.reference:
                    raise QLInputError('Market data in the MarketDataBasket and ProcessBasket have to be equal and in same order!')

    def _generate_process(self) -> ql.StochasticProcess:
        processes: list[ql.StochasticProcess] = []
        for sub_process in self._sub_processes:
            generated_process = sub_process._generate_process()     # pylint: disable=protected-access  # Friends of QLBasketProcess
            assert not isinstance(generated_process, list)
            processes.append(generated_process)
        return processes
