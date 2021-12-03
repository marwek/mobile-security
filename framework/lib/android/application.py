from framework.lib.android.status_page import StatusPage
from framework.lib.common.page_splashscreen import SplashScreenPage
from framework.lib.common.page_license_key import LicenseKeyPage
from framework.lib.common.page_android import AndroidNativePage
from framework.lib.android.virus_page import VirusPage
from framework.lib.android.antitheft_page import AntitheftPage


class AndroidApp:
    def __init__(self, driver):
        self.status_page = StatusPage(driver)
        self.splashscreen_page = SplashScreenPage(driver)
        self.license_key_page = LicenseKeyPage(driver)
        self.native_app = AndroidNativePage(driver)
        self.virus_page = VirusPage(driver)
        self.antitheft_page = AntitheftPage(driver)
