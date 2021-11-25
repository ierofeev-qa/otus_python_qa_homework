import pytest
from selenium import webdriver
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


@pytest.fixture
def main_page_locators():
    return [
        MainPageLocators.HEADER_ICONS,
        MainPageLocators.SEARCH_ITEM,
        MainPageLocators.NAVBAR,
        MainPageLocators.CART_BUTTON,
        MainPageLocators.FOOTER
    ]


@pytest.fixture
def catalog_page_locators():
    return [
        CatalogPageLocators.GROUP_LIST,
        CatalogPageLocators.LIMIT_INPUT,
        CatalogPageLocators.SORT_INPUT,
        CatalogPageLocators.LIST_VIEW_BUTTON,
        CatalogPageLocators.GRID_VIEW_BUTTON
    ]


@pytest.fixture
def product_page_locators():
    return [
        ProductPageLocators.PRODUCT_IMAGES,
        ProductPageLocators.REVIEW_TAB,
        ProductPageLocators.RATING_BUTTONS,
        ProductPageLocators.DESCRIPTION_TAB,
        ProductPageLocators.ADD_TO_CART_BUTTON
    ]


@pytest.fixture
def admin_login_page_locators():
    return [
        AdminLoginPageLocators.LOGIN_BUTTON,
        AdminLoginPageLocators.HEADER,
        AdminLoginPageLocators.USERNAME_INPUT,
        AdminLoginPageLocators.PASSWORD_INPUT,
        AdminLoginPageLocators.HELP_BLOCK
    ]


@pytest.fixture
def registration_page_locators():
    return [
        RegistrationPageLocators.FIRSTNAME_INPUT,
        RegistrationPageLocators.LASTNAME_INPUT,
        RegistrationPageLocators.PASSWORD_INPUT,
        RegistrationPageLocators.EMAIL_INPUT,
        RegistrationPageLocators.CONTINUE_BUTTON
    ]
