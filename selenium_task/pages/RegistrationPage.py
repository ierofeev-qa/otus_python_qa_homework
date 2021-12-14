from .BasePage import BasePage
from selenium.webdriver.common.by import By
import random
import string

test_firstname = 'test_firstname'
test_lastname = 'test_secondname'
test_password = 'test_password'
test_phone = '89996663322'
random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
test_mail = f'test-mail{random_string}@mail.ru'


class RegistrationPage(BasePage):

    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '[id="input-firstname"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '[id="input-lastname"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[id="input-email"]')
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '[id="input-telephone"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="input-password"]')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '[id="input-confirm"]')
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, '[class="pull-right"] [type="checkbox"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    CONFIRM_CONTINUE_BUTTON = (By.CSS_SELECTOR, '[class="pull-right"] [class="btn btn-primary"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="column-right"]//*[contains(text(), "Logout")]')

    def __init__(self, browser):
        super().__init__(browser)
        self.rel_url = '/index.php?route=account/register'

    def register_new_user(
            self,
            first_name: str = test_firstname,
            last_name: str = test_lastname,
            password: str = test_password,
            phone: str = test_phone,
            mail: str = test_mail
    ):
        self.wait_for_element(self.FIRSTNAME_INPUT).send_keys(first_name)
        self.wait_for_element(self.LASTNAME_INPUT).send_keys(last_name)
        self.wait_for_element(self.EMAIL_INPUT).send_keys(mail)
        self.wait_for_element(self.TELEPHONE_INPUT).send_keys(phone)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)
        self.wait_for_element(self.PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.wait_for_element(self.PRIVACY_POLICY_CHECKBOX).click()
        self.wait_for_element(self.CONTINUE_BUTTON).click()
