from appium.webdriver.common.mobileby import MobileBy
from framework.lib.utils.element import element_app
from framework.lib.utils.element import AndroidElement
from framework.lib.common.page_base import PageBase
from framework.lib.utils.locators import LocatorsIds


class LicenseKeyPage(PageBase):

    def __init__(self, driver):
        self.driver = driver
        self.locator = LocatorsIds()

    @element_app
    def button_activate(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.android_button + 'and @text="Activate"]')

    @element_app
    def edit_license(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.fscorp_id + 'and @class="android.widget.EditText"]')

