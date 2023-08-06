from typing import Iterable, Any, TypeVar

DayCount = str
Calendar = str
Currency = str
BusinessConvention = str
PeriodPart = str

ValueType = TypeVar('ValueType')


class Registry(list[ValueType]):
    def __init__(self, item_type: type):
        self._item_type: type = item_type
        super().__init__()

    def register(self, arg: ValueType) -> None:
        assert isinstance(arg, self._item_type), f'Expected {self._item_type} but got {type(arg)}'
        super().append(arg)     # type: ignore[arg-type]

    def register_list(self, arg: Iterable[ValueType]) -> None:
        for item in arg:
            self.register(item)

    def __setitem__(self, key: Any, value: Any) -> None:
        raise NotImplementedError

    def append(self, registry: Any) -> None:
        raise NotImplementedError

    def extend(self, __iterable: Iterable[Any]) -> None:
        raise NotImplementedError


DayCounts: Registry[DayCount] = Registry(DayCount)
Calendars: Registry[Calendar] = Registry(Calendar)
BusinessConventions: Registry[BusinessConvention] = Registry(BusinessConvention)
Currencies: Registry[Currency] = Registry(Currency)

PeriodParts: list[PeriodPart] = ['D', 'W', 'M', 'Y']
