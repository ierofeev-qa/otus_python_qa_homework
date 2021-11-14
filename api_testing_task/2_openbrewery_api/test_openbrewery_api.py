import pytest
import requests
from jsonschema import validate


@pytest.mark.parametrize("path", [
    "/breweries",
    "/breweries?by_type=bar",
    "/breweries/search?query=dog",
    "/breweries?by_city=san_diego"
])
def test_status_code(base_url, path):
    """Check page status code"""
    assert requests.get(base_url + f"{path}").status_code == 200


@pytest.mark.parametrize("expected_number", [None, 30, 50, 51])
def test_results_per_page(base_url, expected_number):
    """Check number of results returned"""
    response = requests.get(base_url + f'/breweries?per_page={expected_number}')
    actual_number = len(response.json())

    if expected_number in (20, 50):
        assert actual_number == expected_number
    elif expected_number is None:
        assert actual_number == 20
    elif expected_number > 50:
        assert actual_number == 50


@pytest.mark.parametrize("city_snake_case, city_camel_case", [
    ('san_diego', 'San Diego'),
    ('new_york', 'New York'),
    ('san_francisco', 'San Francisco'),
], ids=['San Diego', 'New York', 'San Francisco'])
def test_results_by_city(base_url, city_snake_case, city_camel_case):
    """Check results returned by city"""
    result = requests.get(base_url + f'/breweries?by_city={city_snake_case}').json()
    for brewery in result:
        assert city_camel_case in brewery['city']


@pytest.mark.parametrize("filter_value, sorting_type_value, sorting_order", [
    ('by_state=ohio', 'id', 'asc'),
    ('by_city=san_diego', 'name', 'desc')
    ])
def test_sorting(base_url, filter_value, sorting_type_value, sorting_order):
    """Check sorting in result"""
    result = requests.get(base_url + f'/breweries?{filter_value}&sort={sorting_type_value}:{sorting_order}').json()
    actual_result = []

    for brewery in result:
        actual_result.append(brewery[sorting_type_value])

    expected_result = actual_result.copy()

    if sorting_order == 'desc':
        expected_result.sort(reverse=True)
    else:
        expected_result.sort()

    assert actual_result == expected_result


def test_json_schema(base_url):
    """Check if json structure is correct"""
    result = requests.get(base_url + '/breweries').json()

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "city": {"type": "string"},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
        },
        "required": ["id", "name", "city", "postal_code", "country"]
    }

    for brewery in result:
        validate(instance=brewery, schema=schema)
