from appium.common.exceptions import InvalidSwitchToTargetException


class NoSuchContextException(InvalidSwitchToTargetException):
    """
    Thrown when context target to be switched doesn't exist.
    """
    pass
