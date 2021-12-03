import time

from framework.lib.utils.wait import WaitForElement
from appium.webdriver.common.touch_action import TouchAction


class PageObject:
    """General app object"""
    def __init__(self, driver):
        self.driver = driver


class PageBase(PageObject):
    """Base app object model"""

    def tap(self):
        element = self._wait_for_element(self.locator)
        action = TouchAction(self.driver)
        action.tap(element).perform()

    def click(self):
        element = self._wait_for_element(self.locator)
        element.click()
        time.sleep(2)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def send_keys(self, keys):
        element = self._wait_for_element(self.locator)
        element.send_keys(keys)
        time.sleep(1)

    def hide_keyboard(self):
        time.sleep(0.25)
        self.driver.hide_keyboard()

    def is_visible(self):
        element = self._wait_for_element(self.locator)
        element.is_displayed()

    def is_checked(self):
        element = self._wait_for_element(self.locator)
        element.is_selected()

    def get_text(self):
        element = self._wait_for_element(self.locator)
        return element.get_attribute('text')

    def find_elements(self):
        elements = self._wait_for_element(self.locator)
        return elements.find_elements(*self.locator)

    def _wait_for_element(self, locator):
        WaitForElement.wait(self.driver, locator)
        return self.driver.find_element(*locator)

