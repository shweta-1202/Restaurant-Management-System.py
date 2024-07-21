class CustomException(Exception):
    pass
class InvalidMenuItemError(CustomException):
    pass
class InsufficientQuantityError(Exception):
    pass
class DuplicateMenuItemError(Exception):
    pass