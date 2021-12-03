from resources.links import url
from utils.tools import PATH

capabilities = dict(
    platformName='android',
    deviceName='android',
    automationName='UiAutomator2',
    platformVersion='8.0',
    appActivity='com.fsecure.ms.ui.LauncherActivity',
    appPackage='com.fsecure.ms.fscorp',
    app=PATH('../apps/corporate-fsc-oem-android.apk'),
)

license = "REPLACE_WITH_VALID_LICENSE_KEY"

apk_package = 'com.fsecure.ms.fscorp'
app_main_activity = 'com.fsecure.ms.ui.MainActivity'
apk_name = 'corporate-fsc-oem-android.apk'
app_link = url + apk_name