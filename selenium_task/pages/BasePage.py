from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_element(self, locator, timeout=5):
        try:
            return WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element {locator} wasn't found")
