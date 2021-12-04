import pytest
from selenium_task.conftest import (
    wait_element,
    MAIN_PAGE_LOCATORS,
    CATALOG_PAGE_LOCATORS,
    PRODUCT_PAGE_LOCATORS,
    ADMIN_LOGIN_PAGE_LOCATORS,
    REGISTRATION_PAGE_LOCATORS,
)


@pytest.mark.parametrize("rel_url, locators", [
    ('', MAIN_PAGE_LOCATORS),
    ('/index.php?route=product/category&path=24', CATALOG_PAGE_LOCATORS),
    ('/index.php?route=product/product&path=24&product_id=28', PRODUCT_PAGE_LOCATORS),
    ('/admin', ADMIN_LOGIN_PAGE_LOCATORS),
    ('/index.php?route=account/register', REGISTRATION_PAGE_LOCATORS)
], ids=["Main page", "Catalog page", "Product page", "Admin login page", "Registration page"])
def test_elements_are_present(browser, url, rel_url, locators):
    """Check if elements exist on page"""
    browser.get(url + rel_url)

    for element in locators:
        wait_element(element, browser)
