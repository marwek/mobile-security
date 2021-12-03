from enum import IntEnum


class ApplicationState(IntEnum):
    NOT_INSTALLED = 0
    NOT_RUNNING = 1
    RUNNING_IN_BACKGROUND = 2
    RUNNING_IN_FOREGROUND = 3
