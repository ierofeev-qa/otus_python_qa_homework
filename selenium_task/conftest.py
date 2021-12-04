import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium_task.Locators import (
    MainPageLocators,
    CatalogPageLocators,
    ProductPageLocators,
    AdminLoginPageLocators,
    RegistrationPageLocators
)

DRIVERS = 'C:\\Users\\ivane\\Selenium Drivers'


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"],
        help="Set browser to launch"
    )
    parser.addoption("--maximized", action="store_true", help="Maximize browser window")
    parser.addoption("--url", action="store", default="https://demo.opencart.com")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        driver = webdriver.Chrome(executable_path=f'{DRIVERS}\\chromedriver.exe')
    if _browser == "firefox":
        driver = webdriver.Firefox(executable_path=f'{DRIVERS}\\geckodriver')
    if _browser == "opera":
        driver = webdriver.Chrome(executable_path=f'{DRIVERS}\\operadriver')

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver


def wait_element(locator, driver, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))
    except TimeoutException:
        raise AssertionError(f"Element {locator} wasn't found")


MAIN_PAGE_LOCATORS = [
        MainPageLocators.HEADER_ICONS,
        MainPageLocators.SEARCH_ITEM,
        MainPageLocators.NAVBAR,
        MainPageLocators.CART_BUTTON,
        MainPageLocators.FOOTER
    ]

CATALOG_PAGE_LOCATORS = [
        CatalogPageLocators.GROUP_LIST,
        CatalogPageLocators.LIMIT_INPUT,
        CatalogPageLocators.SORT_INPUT,
        CatalogPageLocators.LIST_VIEW_BUTTON,
        CatalogPageLocators.GRID_VIEW_BUTTON
    ]

PRODUCT_PAGE_LOCATORS = [
        ProductPageLocators.PRODUCT_IMAGES,
        ProductPageLocators.REVIEW_TAB,
        ProductPageLocators.RATING_BUTTONS,
        ProductPageLocators.DESCRIPTION_TAB,
        ProductPageLocators.ADD_TO_CART_BUTTON
    ]

ADMIN_LOGIN_PAGE_LOCATORS = [
        AdminLoginPageLocators.LOGIN_BUTTON,
        AdminLoginPageLocators.HEADER,
        AdminLoginPageLocators.USERNAME_INPUT,
        AdminLoginPageLocators.PASSWORD_INPUT,
        AdminLoginPageLocators.HELP_BLOCK
    ]

REGISTRATION_PAGE_LOCATORS = [
        RegistrationPageLocators.FIRSTNAME_INPUT,
        RegistrationPageLocators.LASTNAME_INPUT,
        RegistrationPageLocators.PASSWORD_INPUT,
        RegistrationPageLocators.EMAIL_INPUT,
        RegistrationPageLocators.CONTINUE_BUTTON
    ]
