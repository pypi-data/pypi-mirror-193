
def to_single_type(type_description: str) -> str:
    if type_description.startswith('#') and type_description.endswith('#'):
        return type_description[1:-1].lower()
    return type_description.lower()


def to_list_type(type_description: str) -> str:
    type_description = to_single_type(type_description)
    return type_description[0].upper() + type_description[1:]


def to_matrix_type(type_description: str) -> str:
    type_description = to_single_type(type_description)
    return f'#{type_description.lower()}#'


def is_single(type_description: str) -> bool:
    return type_description == to_single_type(type_description)


def is_list(type_description: str) -> bool:
    return type_description == to_list_type(type_description)


def is_matrix(type_description: str) -> bool:
    return type_description == to_matrix_type(type_description)


Float: str = 'f'
Int: str = 'i'
Bool: str = 'b'
Str: str = 's'
Date: str = 'd'
Reference: str = 'r'
SubStorage: str = 'o'
Period: str = 'period'
Matrix: str = 'matrix'
DayCount: str = 'daycount'
Business: str = 'business'
Calendar: str = 'calendar'
PeriodPart: str = 'periodpart'
Storage: str = 'storage'
NoType: str = 'notype'

Floats: str = to_list_type(Float)
Ints: str = to_list_type(Int)
Bools: str = to_list_type(Bool)
Strs: str = to_list_type(Str)
Dates: str = to_list_type(Date)
References: str = to_list_type(Reference)
SubStorages: str = to_list_type(SubStorage)
Periods: str = to_list_type(Period)
DayCounts: str = to_list_type(DayCount)
Businesses: str = to_list_type(Business)
Calendars: str = to_list_type(Calendar)
Storages: str = to_list_type(Storage)

FloatMatrix: str = to_matrix_type(Float)
IntMatrix: str = to_matrix_type(Int)
# BoolMatrix: str = to_matrix_type(Bool)
# StrMatrix: str = to_matrix_type(Str)
# DateMatrix: str = to_matrix_type(Date)
# ReferenceMatrix: str = to_matrix_type(Reference)
# PeriodMatrix: str = to_matrix_type(Period)
# DayCountMatrix: str = to_matrix_type(DayCount)
# BusinessMatrix: str = to_matrix_type(Business)
# CalendarMatrix: str = to_matrix_type(Calendar)
