from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

from framework.lib.utils.locators import LocatorsIds
from framework.lib.utils.element import element_app
from framework.lib.utils.element import AndroidElement
from framework.lib.common.page_base import PageBase


class AndroidNativePage(PageBase):

    def __init__(self, driver):
        self.driver = driver
        self.locator = LocatorsIds()
    
    @element_app
    def icon_permission(self):
        return AndroidElement(self.driver, MobileBy.ID,
                              self.locator.android_packageinstaller + 'permission_icon')

    @element_app
    def message(self):
        return AndroidElement(self.driver, MobileBy.ID,
                              self.locator.android_packageinstaller + 'permission_message')

    @element_app
    def button_deny(self):
        return AndroidElement(self.driver, MobileBy.ID,
                              self.locator.android_packageinstaller + 'permission_deny_button')

    @element_app
    def button_allow(self):
        return AndroidElement(self.driver, MobileBy.ID,
                              self.locator.android_packageinstaller + 'permission_allow_button')

    @element_app
    def current_text(self):
        return AndroidElement(self.driver, MobileBy.ID,
                              self.locator.android_packageinstaller + 'current_page_text')

    @element_app
    def task_list_view(self):
        return AndroidElement(self.driver, MobileBy.XPATH,
                              '//*[@resource-id="com.android.systemui:id/task_view_bar"]')

    def switch_to_task(self, task_name):
        presence = EC.presence_of_all_elements_located(
            self.driver.find_elements(MobileBy.CLASS_NAME,
                                      '//*[@resource-id="com.android.systemui:id/task_view_bar"]'))
        if presence:
            tasks_list = self.driver.find_elements(MobileBy.CLASS_NAME,
                                                   '//*[@resource-id="com.android.systemui:id/task_view_bar"]')
            for task in tasks_list:
                if task.text.strip() in task_name:
                    task.click()
        return False

