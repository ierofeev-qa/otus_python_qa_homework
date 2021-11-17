import pytest


def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru', help='Url to check response status', required=True)
    parser.addoption('--status_code', help='Expected status code', required=True)


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def expected_status_code(request):
    return request.config.getoption("--status_code")
