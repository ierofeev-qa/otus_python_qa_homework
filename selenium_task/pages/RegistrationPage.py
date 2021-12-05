from .BasePage import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '[id="input-firstname"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '[id="input-lastname"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[id="input-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="input-password"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    rel_url = '/index.php?route=account/register'
