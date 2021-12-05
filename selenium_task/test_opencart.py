import pytest
from selenium_task.pages.MainPage import MainPage
from selenium_task.pages.CatalogPage import CatalogPage
from selenium_task.pages.ProductPage import ProductPage
from selenium_task.pages.AdminLoginPage import AdminLoginPage
from selenium_task.pages.RegistrationPage import RegistrationPage
from selenium_task.pages.BasePage import element_is_present


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
        ProductPage.REVIEW_TAB
    ]),
    (AdminLoginPage, [
        AdminLoginPage.LOGIN_BUTTON,
        AdminLoginPage.HEADER,
        AdminLoginPage.HELP_BLOCK,
        AdminLoginPage.PASSWORD_INPUT,
        AdminLoginPage.USERNAME_INPUT
    ]),
    (RegistrationPage, [
        RegistrationPage.FIRSTNAME_INPUT,
        RegistrationPage.LASTNAME_INPUT,
        RegistrationPage.EMAIL_INPUT,
        RegistrationPage.PASSWORD_INPUT,
        RegistrationPage.CONTINUE_BUTTON
    ])
], ids=["Main page", "Catalog page", "Product page", "Admin login page", "Registration page"])
def test_elements_are_present(browser, url, page_class, locators):
    """Check if elements exist on page"""
    page = page_class(browser)
    browser.get(url + page.rel_url)

    for element in locators:
        element_is_present(element, browser)
