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
def test_elements_are_present(remote, url, page_class, locators):
    """Check if elements exist on page"""
    page = page_class(remote)
    remote.get(url + page.rel_url)

    for element in locators:
        page.wait_for_element(element)


def test_add_item_in_catalogue(remote, url):
    """Check if new product successfully added from admin page"""
    admin_page = AdminPage(remote)
    remote.get(url + admin_page.rel_url)

    admin_page.login()
    admin_page.open_catalog_section('catalog', 'Products')
    admin_page.add_new_product()

    admin_page.wait_for_element(AdminPage.SUCCESS_ALERT)


def test_delete_item_from_catalog(remote, url):
    """Check product deletion from admin page"""
    admin_page = AdminPage(remote)
    remote.get(url + admin_page.rel_url)

    admin_page.login()
    admin_page.delete_product()
    admin_page.wait_for_element(AdminPage.SUCCESS_ALERT)


def test_user_registration(remote, url):
    """Check user registration"""
    registration_page = RegistrationPage(remote)
    remote.get(url + registration_page.rel_url)

    registration_page.register_new_user()
    registration_page.wait_for_element(RegistrationPage.CONFIRM_CONTINUE_BUTTON).click()
    registration_page.wait_for_element(RegistrationPage.LOGOUT_BUTTON)


@pytest.mark.parametrize('locator, currency_symbol', [
    (MainPage.DROPDOWN_EUR_BUTTON, '€'),
    (MainPage.DROPDOWN_GBP_BUTTON, '£'),
    (MainPage.DROPDOWN_USD_BUTTON, '$')
], ids=['EUR', 'GPB', 'USD'])
def test_switch_currency(remote, url, locator, currency_symbol):
    """Check currency switch"""
    main_page = MainPage(remote)
    remote.get(url)

    main_page.open_currency_dropdown()
    main_page.wait_for_element(locator).click()

    assert currency_symbol in main_page.wait_for_element(MainPage.CURRENCY_BUTTON).text
