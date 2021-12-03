from framework.lib.common.page_base import PageBase
from framework.lib.utils.wait import WaitForElement


def element_app(func):
    """Wrapper for function to annotate as python property"""
    def element_call(*args, **kwargs):
        element = func(*args, **kwargs)
        element.name = func.__name__
        return element

    return property(element_call)


class AndroidElement(PageBase):
    def __init__(self, driver, by, val):
        self.driver = driver
        self.locator = (by, val)
