import pytest
from selenium_task.pages.MainPage import MainPage
from selenium_task.pages.CatalogPage import CatalogPage
from selenium_task.pages.ProductPage import ProductPage
from selenium_task.pages.AdminPage import AdminPage
from selenium_task.pages.RegistrationPage import RegistrationPage


@pytest.mark.parametrize("page_class, locators", [
    (MainPage, [
        MainPage.HEADER_ICONS,
        MainPage.NAVBAR,
        MainPage.FOOTER,
        MainPage.CART_BUTTON,
        MainPage.SEARCH_ITEM
    ]),
    (CatalogPage, [
        CatalogPage.GROUP_LIST,
        CatalogPage.LIST_VIEW_BUTTON,
        CatalogPage.GRID_VIEW_BUTTON,
        CatalogPage.LIMIT_INPUT,
        CatalogPage.SORT_INPUT
    ]),
    (ProductPage, [
        ProductPage.PRODUCT_IMAGES,
        ProductPage.ADD_TO_CART_BUTTON,
        ProductPage.DESCRIPTION_TAB,
        ProductPage.RATING_BUTTONS,
        ProductPage.QUANTITY_INPUT
    ]),
    (AdminPage, [
        AdminPage.LOGIN_BUTTON,
        AdminPage.HEADER,
        AdminPage.HELP_BLOCK,
        AdminPage.PASSWORD_INPUT,
        AdminPage.USERNAME_INPUT
    ]),
    (RegistrationPage, [
        RegistrationPage.FIRSTNAME_INPUT,
        RegistrationPage.LASTNAME_INPUT,
        RegistrationPage.EMAIL_INPUT,
        RegistrationPage.PASSWORD_INPUT,
        RegistrationPage.CONTINUE_BUTTON
    ])
], ids=["Main page", "Catalog page", "Product page", "Admin page", "Registration page"])
def test_elements_are_present(browser, url, page_class, locators):
    """Check if elements exist on page"""
    page = page_class(browser)
    browser.get(url + page.rel_url)

    for element in locators:
        page.wait_for_element(element)


def test_add_item_in_catalogue(browser, url):
    """Check if new product successfully deleted from admin page"""
    admin_page = AdminPage(browser)
    browser.get(url + AdminPage.rel_url)

    admin_page.login()
    admin_page.open_catalog_section('catalog', 'Products')
    admin_page.add_new_product()

    admin_page.wait_for_element(AdminPage.SUCCESS_ALERT)


def test_delete_item_from_catalog(browser, url):
    """Check product deletion from admin page"""
    admin_page = AdminPage(browser)
    browser.get(url + AdminPage.rel_url)

    admin_page.login()
    admin_page.delete_product()
    admin_page.wait_for_element(AdminPage.SUCCESS_ALERT)
