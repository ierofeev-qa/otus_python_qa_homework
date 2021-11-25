import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


def wait_element(locator, driver, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))
    except TimeoutException:
        raise AssertionError(f"Element {locator} wasn't found")


@pytest.mark.parametrize("rel_url, locators", [
    ('', 'main_page_locators'),
    ('/index.php?route=product/category&path=24', 'catalog_page_locators'),
    ('/index.php?route=product/product&path=24&product_id=28', 'product_page_locators'),
    ('/admin', 'admin_login_page_locators'),
    ('/index.php?route=account/register', 'registration_page_locators')
], ids=["Main page", "Catalog page", "Product page", "Admin login page", "Registration page"])
def test_elements_are_present(browser, url, rel_url, locators, request):
    elements = request.getfixturevalue(locators)

    browser.get(url + rel_url)

    for element in elements:
        wait_element(element, browser)
