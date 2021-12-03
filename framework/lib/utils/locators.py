
class LocatorsIds:

    @property
    def android_button(self) -> str:
        return '//*[@class="android.widget.Button"' + ' '

    @property
    def android_packageinstaller(self) -> str:
        return 'com.android.packageinstaller:id/'

    @property
    def android_checkbox(self) -> str:
        return '//android.widget.ImageView[@content-desc="checkbox"]'

    @property
    def fscorp_id(self):
        return '//*[@resource-id="com.fsecure.ms.fscorp:id/"' + ' '

    @property
    def carousel_id(self):
        return '(//android.widget.ImageView[@content-desc="Carousel image"])'

    @property
    def toggle_button(self):
        return 'android.widget.CheckBox'

    @property
    def android_settings_cancel_button(self):
        return 'com.android.settings:id/cancel_button'

    @property
    def android_settings_action_button(self):
        return 'com.android.settings:id/action_button'

    @property
    def android_settings_uninstall_button(self):
        return 'com.android.settings:id/uninstall_button'

