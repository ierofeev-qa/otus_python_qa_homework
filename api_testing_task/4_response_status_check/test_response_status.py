import requests


def test_status_code(url, expected_status_code):
    actual_status_code = requests.get(url).status_code
    assert expected_status_code == str(actual_status_code)
