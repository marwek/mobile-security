
import os
import shutil

from requests import get, head
from requests.exceptions import ConnectionError


def app_download(url):
    _current_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    _f = url.split('/')[-1]
    file = _current_path + '/../apps/' + _f

    if head(url).status_code == 200:
        try:
            with get(url, stream=True) as r:
                with open(file, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            return file
        except ConnectionError:
            ConnectionError("Problem with connection")
    else:
        return False
