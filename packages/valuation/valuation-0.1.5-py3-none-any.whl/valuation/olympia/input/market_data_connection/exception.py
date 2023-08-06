from valuation.olympia.input.exception import OlympiaImportError


class OlympiaDataConnectionError(OlympiaImportError):
    pass


class OlympiaBadDataError(OlympiaImportError):
    pass


class ExcelFileParsingError(OlympiaDataConnectionError):
    pass


class CSVFileParsingError(OlympiaDataConnectionError):
    pass
