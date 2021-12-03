from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

from framework.lib.common.page_base import PageBase
from framework.lib.utils.element import element_app, AndroidElement
from framework.lib.utils.locators import LocatorsIds


class VirusPage(PageBase):

    def __init__(self, driver):
        self.driver = driver
        self.locator = LocatorsIds()

    @element_app
    def button_scan_now(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.android_button + 'and @text="Scan now"]')

    @element_app
    def button_settings(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.android_button + 'and @text="Settings"]')
    
    @element_app
    def button_stop_scan(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.android_button + 'and @text="Stop scan"]')

    @element_app
    def button_done(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.android_button + 'and @text="Done"]')

    @element_app
    def button_done(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.android_button + 'and @text="Done"]')

    @element_app
    def image(self):
        return AndroidElement(self.driver, MobileBy.ACCESSIBILITY_ID, 'Feature view image')

    def find_element_text(self, text):
        presence = EC.presence_of_all_elements_located(
            self.driver.find_elements(MobileBy.CLASS_NAME, 'android.widget.TextView'))
        if presence:
            element_list = self.driver.find_elements(MobileBy.CLASS_NAME, 'android.widget.TextView')
            for element in element_list:
                if element.text.strip() in text:
                    return True

