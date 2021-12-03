"""
TC_Antitheft_2 :  `Lock screen` toggle button ON check

Preconditions:
1. `Lock screen` is not enabled

Steps:
1. Go to `Antitheft`
2. Toggle `Lock screen` on
3. Press `Continue` in confirming popup

Expected results:
1. App should display confirming popup for locking screen
2. After pressing `Continue` activation screen should be displayed
"""
from appium import webdriver
from framework.lib.android.application import AndroidApp
from resources.android.resources import capabilities, license, apk_package
from utils.base_test import BaseTestCase


class TC_02_Antitheft_activation_screen(BaseTestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        self.app = AndroidApp(self.driver)

    def test_antitheft_activation_screen(self):
        self.app.splashscreen_page.button_accept.click()
        self.app.native_app.button_allow.click()
        self.app.native_app.button_allow.click()
        self.app.license_key_page.edit_license.send_keys(license)
        self.app.license_key_page.button_activate.click()
        self.app.status_page.antitheft.click()
        self.app.antitheft_page.button_lock_screen.click()
        self.app.antitheft_page.button_continue.click()
        self.app.antitheft_page.button_activation.is_visible()
        self.app.antitheft_page.button_uninstall_app.is_visible()

    def tearDown(self) -> None:
        self.driver.quit()