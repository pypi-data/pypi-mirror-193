class CustomTypeErrorException(Exception):
    """Raised when type(value) is not expected"""
    pass


class CustomFileNotFoundException(Exception):
    """Raised when file or directory is not exist"""
    pass


class CustomFileNameException(Exception):
    """Raised when file or directory has incorrect names"""
    pass


class CustomNotFoundException(Exception):
    """Raised when file or directory has incorrect names"""
    pass


class CustomFormatDataException(Exception):
    """Raised when data is not isascii format"""
    pass


class CustomIncorrectTimeException(Exception):
    """Raised when start data or finish data is incorrect"""
    pass


class CommandLineArgumentsException(Exception):
    """Raised when required arguments was not passed"""
    pass
