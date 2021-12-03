"""
TC_Installation_1: Install app on device

Preconditions:
1. Device does not have software installed
2. Download link for app is accessible
3. Valid license key is provided

Steps:
1. Download software on to disk
2. Run `adb` command to install app
3. Allow app permissions
4. Open app
5. Input license key and activate app

Expected results:
1. App is downloaded and installed
2. License key is entered with success
3. App is activated
4. Status of app is displayed
"""
from appium import webdriver

from framework.lib.android.application import AndroidApp
from resources.android.resources import capabilities
from utils.base_test import BaseTestCase
from utils.app_downloader import app_download
from utils import app_installer as installer


class TC_01_Installation(BaseTestCase):

    def setUp(self) -> None:
        from resources.android.resources import license, app_link
        self.license = license
        self.link = app_link

    def test_download_android_app(self):
        if not app_download(self.link):
            self.fail("Cant download app")

    def test_install_android_app(self):
        if installer.is_installed():
            installer.remove_apk()

        installer.install_apk()

    def test_enter_valid_license_key(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        self.app = AndroidApp(self.driver)
        self.app.splashscreen_page.button_accept.click()
        self.app.native_app.button_allow.click()
        self.app.native_app.button_allow.click()
        self.app.license_key_page.edit_license.send_keys(self.license)
        self.app.license_key_page.button_activate.click()
        self.app.status_page.antivirus.is_visible()
        self.driver.quit()

    def tearDown(self):
        pass
