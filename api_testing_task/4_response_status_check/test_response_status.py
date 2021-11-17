import requests


def test_status_code(url, expected_status_code):
    actual_status_code = requests.get(url, allow_redirects=False).status_code
    assert expected_status_code == str(actual_status_code)
