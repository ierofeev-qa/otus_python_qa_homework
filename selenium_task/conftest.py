import pytest
from selenium import webdriver

DRIVERS = 'C:\\Users\\ivane\\Selenium Drivers'


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"],
        help="Set browser to launch"
    )
    parser.addoption("--maximized", action="store_true", help="Maximize browser window")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


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
