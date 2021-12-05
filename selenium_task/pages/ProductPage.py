from .BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    PRODUCT_IMAGES = (By.CSS_SELECTOR, '[class="thumbnails"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id="button-cart"]')
    DESCRIPTION_TAB = (By.CSS_SELECTOR, '[id="tab-description"]')
    REVIEW_TAB = (By.CSS_SELECTOR, '[id="tab-review"]')
    RATING_BUTTONS = (By.CSS_SELECTOR, '[class="rating"]')

    rel_url = '/index.php?route=product/product&path=24&product_id=28'
