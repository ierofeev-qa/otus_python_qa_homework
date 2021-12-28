import logging
import allure
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium_task.conftest import LOGS_DIR


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        if self.browser.log_to_file:
            os.makedirs(LOGS_DIR, exist_ok=True)
            self.handler = logging.FileHandler(f"{LOGS_DIR}\\{self.browser.test_name}.log")
            self.handler.setFormatter(logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s'))
            self.logger.addHandler(self.handler)
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step("Wait for an element {locator}")
    def wait_for_element(self, locator, timeout=5):
        self.logger.info("Check if element {} is present".format(locator))
        try:
            return WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error("Element {} wasn't found".format(locator))
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name=f'Wait for {locator} element fail',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element {locator} wasn't found")
