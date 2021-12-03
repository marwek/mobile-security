"""
TC_Antivirus_2: Switching app during antivirus scanning

Preconditions:
1. License is valid
2. Antivirus is turn on
3. Scanning is not running
4. Install some applications

Steps:
1.Go to antivirus service
2. Press `Scan now` button
3. Check if `Stop scan` button is enabled
4. Switch app to background
5. Switch app to front
6. Repeat steps 4 and 5 few times
7. Wait until scanning is complete

Expected conditions:
1. Switching app into the background and bringing it to the foreground should be made without impediment
2. Detailed information about scanning should be displayed on the screen
"""
import time

from appium import webdriver

from framework.lib.android.application import AndroidApp
from resources.android.resources import capabilities, license, apk_package
from utils.base_test import BaseTestCase


class TC_02_Antivirus_Background_Switching(BaseTestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        self.app = AndroidApp(self.driver)

    def test_antivirus(self):
        self.app.splashscreen_page.button_accept.click()
        self.app.native_app.button_allow.click()
        self.app.native_app.button_allow.click()
        self.app.license_key_page.edit_license.send_keys(license)
        self.app.license_key_page.button_activate.click()
        self.app.status_page.antivirus.click()
        self.app.virus_page.button_scan_now.click()

        counter = 0
        activity = self.driver.current_activity
        while counter < 3:
            self.driver.background_app(2)
            time.sleep(5)
            assert self.driver.current_activity == activity
            counter += 1

    def tearDown(self) -> None:
        self.driver.quit()
