from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

from framework.lib.common.page_base import PageBase
from framework.lib.utils.element import element_app, AndroidElement
from framework.lib.utils.locators import LocatorsIds


class AntitheftPage(PageBase):

    def __init__(self, driver):
        self.driver = driver
        self.locator = LocatorsIds()

    @element_app
    def button_lock_screen(self):
        return AndroidElement(self.driver, MobileBy.CLASS_NAME, self.locator.toggle_button)

    @element_app
    def button_continue(self):
        return AndroidElement(self.driver, MobileBy.XPATH, self.locator.android_button + 'and @text="Continue"]')

    @element_app
    def button_cancel(self):
        return AndroidElement(self.driver, MobileBy.XPATH, self.locator.android_button + 'and @text="Cancel"]')

    @element_app
    def button_cancel_activation(self):
        return AndroidElement(self.driver, MobileBy.ID, self.locator.android_settings_cancel_button)

    @element_app
    def button_activation(self):
        return AndroidElement(self.driver, MobileBy.ID, self.locator.android_settings_action_button)

    @element_app
    def button_uninstall_app(self):
        return AndroidElement(self.driver, MobileBy.ID, self.locator.android_settings_uninstall_button)
