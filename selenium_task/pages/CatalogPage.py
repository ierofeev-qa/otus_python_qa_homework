from .BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):

    GROUP_LIST = (By.CSS_SELECTOR, '[class="list-group"]')
    SORT_INPUT = (By.CSS_SELECTOR, '[id="input-sort"]')
    LIMIT_INPUT = (By.CSS_SELECTOR, '[id="input-limit"]')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '[id="list-view"]')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '[id="grid-view"]')

    def __init__(self, browser):
        super().__init__(browser)
        self.rel_url = '/index.php?route=product/category&path=24'
