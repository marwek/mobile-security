from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class WaitForElement:
    """
    This class wait for element with specified time.
    If not getting it throws exception.
    """

    @staticmethod
    def wait(driver, id, timeout=60):
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(id)
            )
        except TimeoutException:
            print('Not able to find element with ID:' + str(id))
