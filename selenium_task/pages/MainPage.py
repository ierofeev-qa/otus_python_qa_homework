from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    HEADER_ICONS = (By.CSS_SELECTOR, '[id="top-links"]')
    NAVBAR = (By.CSS_SELECTOR, '[class="navbar"]')
    SEARCH_ITEM = (By.CSS_SELECTOR, '[id="search"]')
    CART_BUTTON = (By.CSS_SELECTOR, '[id="cart"]')
    FOOTER = (By.CSS_SELECTOR, 'footer [class="container"]')

    rel_url = ''
