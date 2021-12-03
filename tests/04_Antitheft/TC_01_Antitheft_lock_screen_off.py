"""
TC_Antitheft_1 :  `Lock screen` toggle button OFF check

Preconditions:
1. `Lock screen` is not enabled

Steps:
1. Go to `Antitheft`
2. Toggle `Lock screen` on
3. Press `Cancel` in confirming popup

Expected results:
1. App should display confirming popup for locking screen
2. After canceling `Lock screen` button should not be on
"""
from appium import webdriver

from framework.lib.android.application import AndroidApp
from resources.android.resources import capabilities, license, apk_package
from utils.base_test import BaseTestCase


class TC_01_Antitheft_lock_screen_off(BaseTestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        self.app = AndroidApp(self.driver)

    def test_antitheft_lock_screeen(self):
        self.app.splashscreen_page.button_accept.click()
        self.app.native_app.button_allow.click()
        self.app.native_app.button_allow.click()
        self.app.license_key_page.edit_license.send_keys(license)
        self.app.license_key_page.button_activate.click()
        self.app.status_page.antitheft.click()
        self.app.antitheft_page.button_lock_screen.click()
        self.app.antitheft_page.button_cancel.click()
        if self.app.antitheft_page.button_lock_screen.is_checked():
            assert False

    def tearDown(self) -> None:
        self.driver.quit()
