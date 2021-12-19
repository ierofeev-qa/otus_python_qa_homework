from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    HEADER_ICONS = (By.CSS_SELECTOR, '[id="top-links"]')
    NAVBAR = (By.CSS_SELECTOR, '[class="navbar"]')
    SEARCH_ITEM = (By.CSS_SELECTOR, '[id="search"]')
    CART_BUTTON = (By.CSS_SELECTOR, '[id="cart"]')
    FOOTER = (By.CSS_SELECTOR, 'footer [class="container"]')
    CURRENCY_BUTTON = (By.XPATH, '//*[@id="form-currency"]//div[1]')
    DROPDOWN_EUR_BUTTON = (By.CSS_SELECTOR, '[class="dropdown-menu"] [name="EUR"]')
    DROPDOWN_GBP_BUTTON = (By.CSS_SELECTOR, '[class="dropdown-menu"] [name="GBP"]')
    DROPDOWN_USD_BUTTON = (By.CSS_SELECTOR, '[class="dropdown-menu"] [name="USD"]')
    CARD_TOTAL = (By.CSS_SELECTOR, '[id="cart-total"]')

    def __init__(self, browser):
        super().__init__(browser)
        self.rel_url = ''

    def is_currency_dropdown_opened(self):
        self.logger.info("Check if currency dropdown is opened")
        return self.wait_for_element(self.CURRENCY_BUTTON).get_attribute('class') == 'btn-group open'

    def open_currency_dropdown(self):
        self.logger.info("Open currency dropdown")
        if not self.is_currency_dropdown_opened():
            self.wait_for_element(self.CURRENCY_BUTTON).click()
