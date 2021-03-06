from .BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    PRODUCT_IMAGES = (By.CSS_SELECTOR, '[class="thumbnails"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id="button-cart"]')
    DESCRIPTION_TAB = (By.CSS_SELECTOR, '[id="tab-description"]')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '[id="input-quantity"]')
    RATING_BUTTONS = (By.CSS_SELECTOR, '[class="rating"]')

    def __init__(self, browser):
        super().__init__(browser)
        self.rel_url = '/index.php?route=product/product&path=24&product_id=28'
