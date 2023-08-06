from __future__ import annotations

from functools import wraps
from typing import Any, Callable, Optional, TypeVar, Union

import QuantLib as ql

from valuation.consts import signatures, types
from valuation.consts import fields
from valuation.exceptions import DAAException, ProgrammingError, daa_warn
from valuation.global_settings import __type_checking__
from valuation.engine.check import Check, CheckMatrix, ContainedIn, Equals, ObjectType
from valuation.engine.documentation import Documentation
from valuation.engine.exceptions import QLInputError, QLInputWarning
from valuation.engine.mappings import BusinessMap, CalendarMap, DayCountMap
from valuation.engine.utils import date2qldate
from valuation.universal_transfer import DefaultParameters, NoValue, Reference, STORAGE_ID_SEPARATOR, Signature, Storage, \
    StorageTypes, TypeKey
from valuation.utils.other import listify

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from .data_base import QLObjectDB
    from .mappings import AugmentedDict

QuantlibType = Any  # pylint: disable=invalid-name


def single_convert(variable_type: str,  # pylint: disable=too-many-return-statements
                   value: Union[QLObject, StorageTypes.GeneralEntry, None],
                   ql_db: QLObjectDB,
                   factory: dict[Signature, type[QLObjectBase]],
                   default_parameters: list[Storage],
                   master_object: Union[QLObject, QLObjectBase, None],
                   data_only_mode: bool) -> Union[QuantlibType, QLObject]:
    if variable_type in (types.Str, types.Float, types.Int, types.Bool, types.Period, types.Matrix, types.Storage):
        return value
    if variable_type == types.Reference:
        if isinstance(value, QLObject):
            return value
        if isinstance(value, Storage):
            count = 0
            while True:
                new_id: str = f'{master_object.id}{STORAGE_ID_SEPARATOR}{count}'  # type: ignore[union-attr]  # Ensures, that we operate on QLObjects only!
                if Reference(value[fields.Type], new_id) not in ql_db:  # type: ignore[arg-type]
                    break
                count += 1
            value.assign_post_mutable_id(new_id)
            return ql_db.generate_single_entry(value, data_only_mode)
        return ql_db.get(value, data_only_mode)  # type: ignore
    if variable_type == types.Date:
        return value if isinstance(value, ql.Date) else date2qldate(value)  # type: ignore[arg-type]
    if variable_type == types.DayCount:
        return value if isinstance(value, ql.DayCounter) else DayCountMap[value]  # type: ignore[index]
    if variable_type == types.Calendar:
        return value if isinstance(value, ql.Calendar) else CalendarMap[value]  # type: ignore[index]
    if variable_type == types.Business:
        return BusinessMap[value] if isinstance(value, str) else value
    if variable_type == types.SubStorage:
        assert value.signature in factory, f'{value.signature} not in {[str(entry) for entry in factory]}'  # type: ignore[union-attr]
        line_object: QLObjectBase = factory[value.signature](value, ql_db, default_parameters,
                                                             # type: ignore[union-attr, arg-type]
                                                             data_only_mode=data_only_mode,
                                                             master_object=master_object)  # type: ignore[arg-type]
        if __debug__:
            master_object.append_to_debugonly_line_objects(line_object)  # type: ignore[union-attr]
        return line_object
    raise ProgrammingError(f'Unknown Type {variable_type}')


def convert(variable_type: str, value: Union[QLObject, StorageTypes.GeneralEntry, None], ql_db: QLObjectDB,
            factory: dict[Signature, type[QLObjectBase]], default_parameters: list[Storage],
            master_object: Union[QLObject, QLObjectBase, None], data_only_mode: bool) -> Union[QuantlibType, QLObject, list[QLObject]]:
    if value is None:
        return value
    if types.is_single(variable_type):
        return single_convert(variable_type, value, ql_db, factory, default_parameters, master_object, data_only_mode)
    return [
        single_convert(types.to_single_type(variable_type), entry, ql_db, factory, default_parameters, master_object,
                       # type: ignore[arg-type]
                       data_only_mode) for entry in value]  # type: ignore[union-attr]


class QLObjectBaseFinishInit(type):
    """Meta-class, which does two things:
    *   After init no additional data from the storage via the self.data(???) interface can be fetched (__debug__ mode only)
    *   _post_init is called in order to tidy up."""

    def __call__(cls: type[QLObjectBase], *args: Any, **kwargs: Any) -> QLObjectBase:  # type: ignore[misc]
        obj: QLObjectBase = type.__call__(cls, *args, **kwargs)
        assert obj._data_initialization_allowed
        if __debug__:
            obj._data_initialization_allowed = False
            if not obj._documentation_mode and not obj._data_only_mode:
                obj._post_init()
        elif not obj._data_only_mode:
            obj._post_init()
        assert not obj._initialization_finished
        obj._allow_static_usage = True
        obj._initialization_finished = True
        return obj


class classproperty(property):  # pylint: disable=invalid-name

    def __get__(self, obj: Any, objtype: Any = None) -> Any:
        return super().__get__(objtype)


class QLObjectBase(metaclass=QLObjectBaseFinishInit):
    """STYLE-GUIDE:
    *   the access to the storage is just allowed via the functions data() and data_matrix()        (mandatory)
    *   all instance variables shall be protected                                                   (mandatrory)
    *   access to variables should be via properties                                                (exceptions in rare cases allowed)
    *   properties can be found at the beginning of a class, then __init__ then _post_init          (mandatory)
    *   __init__ and _post_init should build a bracket structure, i.e:                              (mandatory)
    *       __init__[Parent] --> __init__[Child] --> _post_init[Child] --> _post_init[Parent]
    *       The last entry in this line is omitted, if _post_init is not set in the parent class
    """
    _signature = signatures.empty

    @classproperty
    def signature(cls) -> Signature:  # pylint: disable=no-self-argument
        return cls._signature

    @classproperty
    def object_type(cls) -> str:  # pylint: disable=no-self-argument
        return cls._signature.type

    @classproperty
    def sub_type(cls) -> str:  # pylint: disable=no-self-argument
        return cls._signature.sub_type

    @classproperty
    def virtual(cls) -> bool:  # pylint: disable=no-self-argument
        return cls._signature == signatures.empty

    @property
    def ql_db(self) -> QLObjectDB:
        return self._ql_db

    @property
    def valuation_date(self) -> ql.Date:
        return self._valuation_date

    @property
    def initialization_finished(self) -> bool:
        return self._initialization_finished

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        self._initialization_finished: bool = False
        self._data_initialization_allowed = True
        if not __debug__ and not data and not ql_db:
            raise DAAException('Documentation mode just allowed in Debug environment!')
        self._documentation_mode = not data and not ql_db
        if __debug__:
            self._debug_only_key_used: set[TypeKey] = set()

        if self._documentation_mode:
            self._documentation: Documentation = Documentation()

        self._data: Storage = data
        self._master_object: Optional[QLObject] = master_object
        self._data_only_mode: bool = data_only_mode
        if default_parameters is None:
            self._default_parameters: list[Storage] = []
        elif isinstance(default_parameters, Storage):
            self._default_parameters = [default_parameters]
        else:
            self._default_parameters = default_parameters
        self._augmented_default_parameters = [data] + self._default_parameters
        self._ql_db: QLObjectDB = ql_db
        if ql_db is not None:
            self._valuation_date: ql.Date = ql_db.valuation_date
        if __debug__ and self._documentation_mode:
            self._valuation_date = NoValue(fields.ValuationDate)

        self._factory: dict[Signature, type[QLObjectBase]] = {}

        __ = self.data(fields.Type, check=Equals(self.object_type))
        if self.sub_type != '':
            __ = self.data(fields.SubType(self.object_type), check=Equals(self.sub_type))  # noqa: F841

        self._allow_static_usage: bool

    def _post_init(self) -> None:
        pass

    def check(self, value: Any, additional_check: Check) -> None:
        if __debug__:
            if self._documentation_mode:
                self._documentation.standard_addcheck(value, additional_check)
            else:
                try:
                    additional_check(value)
                except QLInputWarning as warning:
                    warning.set_additional_information(str(self))
                    daa_warn(str(warning))

    def data_matrix(self, type_key: TypeKey, row_type: str, col_type: str, content_type: str,
                    row_check: Union[None, Check, list[Check]] = None,
                    col_check: Union[None, Check, list[Check]] = None,
                    content_check: Union[None, Check, list[Check]] = None,
                    matrix_check: Union[None, CheckMatrix, list[CheckMatrix]] = None) -> tuple[list[QuantlibType], list[QuantlibType], list[list[QuantlibType]]]:
        """
        Only way to retrieve matrix data from the storage.
        """
        matrix = self.data(type_key, default_value=NoValue(), check=None, allow_fallback_to_default_parameters=False)
        if isinstance(matrix, NoValue) and not self._documentation_mode:
            raise QLInputError(type_key)
        row_headers = list(matrix.row_headers)
        column_headers = list(matrix.column_headers)
        content = [list(line) for line in matrix.content]

        if __debug__:
            row_checks: list[Check] = listify(row_check)
            col_checks: list[Check] = listify(col_check)
            content_checks: list[Check] = listify(content_check)
            matrix_checks: list[CheckMatrix] = listify(matrix_check)

            if self._documentation_mode:
                self._documentation.matrix(type_key, row_type, col_type, content_type, row_checks, col_checks,
                                           content_checks, matrix_checks)

            if not self._documentation_mode:
                if row_type != matrix.row_header_type:
                    raise QLInputError('Wrong type for matrix row header')
                if col_type != matrix.column_header_type:
                    raise QLInputError('Wrong type for matrix column header')
                if content_type != matrix.content_type:
                    raise QLInputError('Wrong type for matrix content')
                for sub_check in row_checks:
                    sub_check(row_headers)
                for sub_check in col_checks:
                    sub_check(column_headers)
                for sub_check in content_checks:
                    for line in content:
                        sub_check(list(line))
                for sub_check in matrix_checks:  # type: ignore
                    sub_check(matrix)
        if not self._documentation_mode:
            if row_type == types.References:
                row_headers = [self.ql_db[reference] for reference in row_headers]
            if col_type == types.References:
                column_headers = [self.ql_db[reference] for reference in column_headers]

        return row_headers, column_headers, content

    def data(self, type_key: TypeKey,
             default_value: Union[QLObject, StorageTypes.GeneralEntry, NoValue, None] = NoValue(),
             check: Union[None, Check, list[Check]] = None, allow_fallback_to_default_parameters: bool = False,
             ql_map: Optional[AugmentedDict[QuantlibType, QuantlibType]] = None,
             ignore_data_only_mode: bool = False) -> QuantlibType:
        """
        Only way to retrieve data from the storage.
        Execution order is:
            look in its own storage, return if available
            look in the fallback storage, return if available
            look at the default_value, return if available
            raise error.
        """
        if not self._data_initialization_allowed:
            raise ProgrammingError('Do not access storage outside of init!')
        if __debug__:
            checks: list[Check] = listify(check)
            if ql_map:
                checks.append(ContainedIn(ql_map))
            if self._documentation_mode:
                self._documentation.standard(type_key, default_value, allow_fallback_to_default_parameters, checks)
                return NoValue(type_key)
            self._debug_only_key_used.add(type_key)
        if self._data_only_mode and not ignore_data_only_mode and type_key.type in (
                types.Reference, types.References, types.Storage, types.Storages):
            return NoValue(type_key)
        if type_key in self._data:
            result = convert(type_key.type, self._data[type_key], self._ql_db, self._factory,
                             self._augmented_default_parameters, self, type_key.allow_data_only_mode)
        elif allow_fallback_to_default_parameters and any(type_key in storage for storage in self._default_parameters):
            for storage in self._default_parameters:
                if type_key in storage:
                    result = convert(type_key.type, storage[type_key], self._ql_db, self._factory,
                                     self._augmented_default_parameters, self, type_key.allow_data_only_mode)
                    if __debug__ and self._master_object and storage.reference == self._master_object.reference:
                        self._master_object._debug_only_key_used.add(
                            type_key)  # pylint: disable=protected-access   # Friend of QLObjectBase
                    break
        elif not isinstance(default_value, NoValue):
            result = convert(type_key.type, default_value, self._ql_db, self._factory,
                             self._augmented_default_parameters, self, type_key.allow_data_only_mode)
        elif not self._documentation_mode:
            raise QLInputError(f'Missing key {type_key}')
        else:
            return default_value
        if __debug__:
            try:
                if not self._documentation_mode:
                    for sub_check in checks:
                        sub_check(result)
            except QLInputWarning as exception:
                exception.set_additional_information(str(self))
                exception.set_additional_information(str(type_key))
                daa_warn(str(exception))
            except DAAException as exception:
                exception.set_additional_information(str(type_key))
                raise exception
            except Exception as exception:
                raise exception
        if ql_map:
            return ql_map[result]
        return result

    def __str__(self) -> str:
        return str(self.signature)

    if __debug__:
        @property
        def document(self) -> Documentation:
            return self._documentation

        def given_but_not_requested(self) -> list[str]:
            return [f'{type_key}:\t{self._data[type_key]}' for type_key in self._data if
                    type_key not in self._debug_only_key_used and type_key.as_list_or_single() not in self._debug_only_key_used and type_key.as_storage_or_reference() not in self._debug_only_key_used]


ReturnType = TypeVar('ReturnType')
DecoratedFunction = Callable[..., ReturnType]


class QLObject(QLObjectBase):  # pylint: disable=abstract-method
    _supported_greeks: tuple[str, ...] = tuple()

    @staticmethod
    def static(func: DecoratedFunction[ReturnType]) -> DecoratedFunction[ReturnType]:
        """
        Decorator to indicate that the return content of the decorated functions or properties is of static nature,
        meaning it won't change over the runtime.
        As we allow market data to change it's state on runtime (e.g. for greeks) we need to track if some data was
        used whose changes are not recognized.
        """

        @wraps(func)
        def wrapper(cls: QLObject, *args: Any, **kwargs: Any) -> ReturnType:
            if cls._listens_for_observers:  # pylint: disable=protected-access
                for observer in cls.observers:
                    assert isinstance(observer, QLObject)
                    if not observer.allow_static_usage:
                        observer.blacklist_market_data(cls)
                # self.reset_observers()  # if we keep the safe usage as it is right now we can't delete the oververs after checking
            return func(cls, *args, **kwargs)

        return wrapper

    @staticmethod
    def moves_to_shifted(func: DecoratedFunction[ReturnType]) -> DecoratedFunction[ReturnType]:
        @wraps(func)
        def wrapper(self: QLObject, *args: Any, **kwargs: Any) -> ReturnType:
            return func(self.state, *args, **kwargs)  # type: ignore[call-arg, attr-defined]

        return wrapper

    @property
    def id(self) -> str:  # pylint: disable=invalid-name
        return self._id

    @property
    def market_data_objects(self) -> set[QLObject]:
        return self._market_data_objects

    @property
    def reference(self) -> Reference:
        return Reference(self.object_type, self._id)

    @property
    def supported_greeks(self) -> tuple[str, ...]:
        return self._supported_greeks

    @property
    def allow_static_usage(self) -> bool:
        return self._allow_static_usage

    @property
    def observers(self) -> list[QLObject]:
        return self._observers

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, None, data_only_mode=data_only_mode)
        if __debug__:
            self._debugonly_line_objects: list[QLObjectBase] = []
        self._id: str = self.data(fields.Id)  # pylint: disable=invalid-name
        self._market_data_objects: set[QLObject] = set()

        self._allow_static_usage = False
        self._observers: list[QLObject] = []
        self._listens_for_observers: bool = True
        self._blacklisted_greeks: set[Reference] = set()

    def reset_observers(self) -> None:
        self._observers = []

    def blacklist_market_data(self, ql_object: QLObject) -> None:
        self._blacklisted_greeks.add(ql_object.reference)
        if ql_object in self._market_data_objects:
            self._market_data_objects.remove(ql_object)

    def add_linetype(self, line_class: type[QLObjectBase], type_key: TypeKey) -> None:
        """
        Each new !possible! substorage which can be found in the storage must be registered here.
        """
        self._factory[line_class.signature] = line_class

        if self._documentation_mode:
            self._documentation.multi_line(type_key, line_class.signature,
                                           line_class(None, None, None, None).document)  # type: ignore[arg-type]

    if __debug__:
        def append_to_debugonly_line_objects(self, ql_object: QLObjectBase) -> None:
            self._debugonly_line_objects.append(ql_object)

    def data(self, type_key: TypeKey,  # pylint: disable=arguments-differ
             default_value: Union[QLObject, StorageTypes.GeneralEntry, NoValue, None] = NoValue(),
             check: Union[None, Check, list[Check]] = None,
             allow_fallback_to_default_parameters: bool = False,
             ql_map: Optional[AugmentedDict[QuantlibType, QuantlibType]] = None,
             ignore_data_only_mode: bool = False,
             exclude_from_greeks: bool = False) -> QuantlibType:
        value = super().data(type_key, default_value, check, allow_fallback_to_default_parameters, ql_map,
                             ignore_data_only_mode)
        if isinstance(value, QLObject) and not exclude_from_greeks:
            if value.supported_greeks:
                self._market_data_objects.add(value)
            self._market_data_objects.update(value.market_data_objects)
            value._observers.append(self)  # pylint: disable=protected-access
        return value

    def market_data(self, greek: str) -> set[Reference]:
        result: set[Reference] = set()
        if greek in self._supported_greeks:
            result.add(self.reference)
        for market_data_object in self._market_data_objects:
            result.update(market_data_object.market_data(greek))
        return result

    def __str__(self) -> str:
        return f'{self.signature}|{self._id}'

    if __debug__:
        def given_but_not_requested(self) -> list[str]:
            result = super().given_but_not_requested()
            for count, line_object in enumerate(self._debugonly_line_objects):
                if sub_result := line_object.given_but_not_requested():
                    for line in sub_result:
                        result.append(f'LineObject {count}:\t{line}')
            return result


class QLAlias(QLObject):  # pylint: disable=abstract-method
    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:  # pylint: disable=super-init-not-called
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        assert self.sub_type == 'Alias'
        real_object: QLObject = self.data(fields.RealObject,
                                          check=ObjectType(Signature(self.object_type, Signature.ALL)))
        if not self._documentation_mode:
            self._ql_db.set_alias(self.reference, real_object)
