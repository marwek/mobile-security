import os

from ppadb.client import Client as AdbClient
from ppadb import InstallError

from resources.android.resources import apk_name, apk_package


def install_apk(device=None):
    client = AdbClient()
    apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '/../apps/'
    if not client.devices()[0].install(apk_path + apk_name):
        raise InstallError
    return True


def remove_apk(device=None):
    client = AdbClient()
    if not client.devices()[0].uninstall(apk_package):
        raise Exception("Package can't be uninstalled")


def is_installed(package='com.fsecure.ms.fscorp'):
    client = AdbClient()
    return client.devices()[0].is_installed(package)
