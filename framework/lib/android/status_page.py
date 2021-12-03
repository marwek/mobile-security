from framework.lib.common.page_base import PageBase
from appium.webdriver.common.mobileby import MobileBy
from framework.lib.utils.element import element_app, AndroidElement
from framework.lib.utils.locators import LocatorsIds


class StatusPage(PageBase):

    def __init__(self, driver):
        self.driver = driver
        self.locator = LocatorsIds()

    @element_app
    def antivirus(self) :
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.carousel_id + '[1]')

    @element_app
    def antitheft(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.carousel_id + '[2]')

    @element_app
    def application_privacy(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.carousel_id + '[3]')

    @element_app
    def safe_browsing(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.carousel_id + '[4]')

    @element_app
    def banking_protection(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.carousel_id + '[5]')

    @element_app
    def statistics(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.carousel_id + '[6]')

