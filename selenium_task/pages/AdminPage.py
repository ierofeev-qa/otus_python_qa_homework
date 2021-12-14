from typing import Tuple
from .BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):

    HEADER = (By.CSS_SELECTOR, '[class="navbar-header"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '[id="input-username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="input-password"]')
    HELP_BLOCK = (By.CSS_SELECTOR, '[class="help-block"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-primary"]')

    ADD_NEW_ITEM_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '[id="input-name1"]')
    META_TAG_INPUT = (By.CSS_SELECTOR, '[id="input-meta-title1"]')
    MODEL_INPUT = (By.CSS_SELECTOR, '[id="input-model"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Save"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Delete"]')

    FILTER_NAME_INPUT = (By.CSS_SELECTOR, '[name="filter_name"]')
    FILTER_MODEL_INPUT = (By.CSS_SELECTOR, '[name="filter_model"]')
    FILTER_BUTTON = (By.CSS_SELECTOR, '[id="button-filter"]')
    SELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, '[class="panel-body"] [id="form-product"] thead [type="checkbox"]')
    SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')

    def __init__(self, browser):
        super().__init__(browser)
        self.rel_url = '/admin'

    @staticmethod
    def get_section_locator(primary_section_name) -> Tuple[str, str]:
        return (
            By.XPATH, f'//*[@id="menu"]/*[@id="menu-{primary_section_name}"]//*[@data-toggle="collapse"]'
        )

    @staticmethod
    def get_sub_section_locator(primary_section_name: str, sub_section_name) -> Tuple[str, str]:
        return (
            By.XPATH, f'//*[@id="menu"]/*[@id="menu-{primary_section_name}"]//*[contains(text(), "{sub_section_name}")]'
        )

    @staticmethod
    def get_add_product_tab_locator(tab_name: str) -> Tuple[str, str]:
        return (
            By.XPATH, f'//*[@class="nav nav-tabs"]//*[contains(text(), "{tab_name}")]/parent::li'
        )

    def login(self, username='user', password='bitnami'):
        self.wait_for_element(self.USERNAME_INPUT).send_keys(username)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)
        self.wait_for_element(self.LOGIN_BUTTON).click()

    def is_section_collapsed(self, section_name):
        return \
            self.wait_for_element(self.get_section_locator(section_name)).get_attribute('class') == 'parent collapsed'

    def open_catalog_section(self, primary_section_name: str, sub_section_name: str):
        if self.is_section_collapsed(primary_section_name):
            self.wait_for_element(self.get_section_locator(primary_section_name)).click()
        self.wait_for_element(self.get_sub_section_locator(primary_section_name, sub_section_name)).click()

    def is_add_product_tab_active(self, tab_name):
        return self.wait_for_element(self.get_add_product_tab_locator(tab_name)).get_attribute('class') == 'active'

    def switch_add_product_tab(self, tab_name):
        if not self.is_add_product_tab_active(tab_name):
            self.wait_for_element(self.get_add_product_tab_locator(tab_name)).click()

    def add_new_product(
            self, product_name: str = 'Test_product_name', meta_tag: str = 'Test_meta_tag', model: str = 'Test_model'
    ):
        self.wait_for_element(self.ADD_NEW_ITEM_BUTTON).click()
        self.switch_add_product_tab('General')
        self.wait_for_element(self.PRODUCT_NAME_INPUT).send_keys(product_name)
        self.wait_for_element(self.META_TAG_INPUT).send_keys(meta_tag)
        self.switch_add_product_tab('Data')
        self.wait_for_element(self.MODEL_INPUT).send_keys(model)
        self.wait_for_element(self.SAVE_BUTTON).click()

    def search_for_a_product(self, product_name: str = 'Test_product_name', model: str = 'Test_model'):
        self.open_catalog_section('catalog', 'Products')
        self.wait_for_element(self.FILTER_NAME_INPUT).send_keys(product_name)
        self.wait_for_element(self.FILTER_MODEL_INPUT).send_keys(model)
        self.wait_for_element(self.FILTER_BUTTON).click()

    def delete_product(self, product_name: str = 'Test_product_name', model: str = 'Test_model'):
        self.search_for_a_product(product_name, model)
        self.wait_for_element(self.SELECT_ALL_CHECKBOX).click()
        self.wait_for_element(self.DELETE_BUTTON).click()
        alert = self.browser.switch_to.alert
        alert.accept()
