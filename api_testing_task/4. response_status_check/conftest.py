import pytest


def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru', help='Url to check response status')
    parser.addoption('--status_code', help='Expected status code')


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

