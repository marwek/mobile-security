from appium.webdriver.common.mobileby import MobileBy
from framework.lib.utils.locators import LocatorsIds
from framework.lib.utils.element import element_app
from framework.lib.utils.element import AndroidElement
from framework.lib.common.page_base import PageBase


class SplashScreenPage(PageBase):
    """Splash screen page"""

    frame = '//android.widget.FrameLayout//android.widget.ScrollView'

    def __init__(self, driver):
        self.driver = driver
        self.locator = LocatorsIds()

    @element_app
    def checkbox_improve_usage_data(self):
        return AndroidElement(self.driver, MobileBy.XPATH, self.locator.android_checkbox)
    
    @element_app
    def button_accept(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.locator.android_button + 'and @text="Accept and continue"]')

    @element_app
    def edit_license(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              self.frame + '//*[@class="android.widget.EditText"]')
