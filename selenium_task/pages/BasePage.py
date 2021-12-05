from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, browser):
        self.browser = browser


def element_is_present(locator, driver, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))
    except TimeoutException:
        raise AssertionError(f"Element {locator} wasn't found")
