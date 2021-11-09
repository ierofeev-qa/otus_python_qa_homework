import requests


def test_status_code(url, status_code):
    assert status_code == str(requests.get(url).status_code)
