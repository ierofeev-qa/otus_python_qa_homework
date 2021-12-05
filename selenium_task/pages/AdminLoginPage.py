from .BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):
    HEADER = (By.CSS_SELECTOR, '[class="navbar-header"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '[id="input-username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="input-password"]')
    HELP_BLOCK = (By.CSS_SELECTOR, '[class="help-block"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-primary"]')

    rel_url = '/admin'
