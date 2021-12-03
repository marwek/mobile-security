"""
TC_Antivirus_1: Running antivirus after clean installation

Preconditions:
1. App is installed and license key is provided
2. Antivirus service was not yet ran

Steps:
1. Open F-Secure Mobile Security app
2. Go to `Antivirus` service
3. Press `Manual scan recommended` link

Expected results:
1. Last scan should have status `never`
2. Icons should have status `X` in red color
3. Manual scan recommendation info field should have gray color
4. Recommendation text should be displayed on screen
"""
from appium import webdriver

from framework.lib.android.application import AndroidApp
from resources.android.resources import capabilities, license
from utils.base_test import BaseTestCase


class TC_01_Antivirus_Running(BaseTestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        self.app = AndroidApp(self.driver)
        self.text_to_find = ['Manual scan recommended', 'Antivirus is on', 'Last scan never']

    def test_antivirus(self):
        self.app.splashscreen_page.button_accept.click()
        self.app.native_app.button_allow.click()
        self.app.native_app.button_allow.click()
        self.app.license_key_page.edit_license.send_keys(license)
        self.app.license_key_page.button_activate.click()
        self.app.status_page.antivirus.click()
        if not self.app.virus_page.find_element_text(self.text_to_find):
            assert False

    def tearDown(self) -> None:
        self.driver.quit()
