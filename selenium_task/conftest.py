import pytest
import logging
import os

from selenium import webdriver


DRIVERS = 'C:\\Users\\ivane\\Selenium Drivers'
LOGS_DIR = 'C:\\Users\\ivane\\PycharmProjects\\otus_python_qa_homework\\selenium_task\\logs'

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"],
        help="Set browser to launch"
    )
    parser.addoption("--maximized", action="store_true", help="Maximize browser window")
    parser.addoption("--url", action="store", default="http://192.168.0.112:8081")
    parser.addoption("--log_level", action="store", default="WARNING")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):
    _browser = request.config.getoption("--browser")
    maximized = request.config.getoption("--maximized")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger('BrowserLogger')
    logger.setLevel(level=log_level)

    test_name = request.node.name

    handler = logging.FileHandler(f"{LOGS_DIR}\\{test_name}.log")
    handler.setFormatter(logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s'))
    logger.addHandler(handler)

    logger.info("--> TEST '{}' STARTED".format(test_name))

    driver = None

    if _browser == "chrome":
        driver = webdriver.Chrome(executable_path=f'{DRIVERS}\\chromedriver.exe')
    if _browser == "firefox":
        driver = webdriver.Firefox(executable_path=f'{DRIVERS}\\geckodriver')
    if _browser == "opera":
        driver = webdriver.Chrome(executable_path=f'{DRIVERS}\\operadriver')

    if maximized:
        driver.maximize_window()

    driver.test_name = test_name
    driver.log_level = log_level

    logger.info("Browser '{}' started".format(_browser))

    def final():
        driver.quit()
        logger.info("--> TEST '{}' FINISHED\n".format(test_name))
        logger.handlers.clear()

    request.addfinalizer(final)

    return driver
