import pytest
import requests
from jsonschema import validate


@pytest.mark.parametrize("path", [
    "/breeds/list/all",
    "/breeds/image/random",
    "/breed/hound/images"
])
def test_status_code(base_url, path):
    """Check page status code"""
    assert requests.get(base_url + f"{path}").status_code == 200


def test_all_breeds_list(base_url, breeds_list):
    """Check if breeds list is equal to the etalon"""
    response = requests.get(base_url + "/breeds/list/all")
    assert response.json()["message"] == breeds_list


@pytest.mark.parametrize("path", [
    "/breeds/list/all",
    "/breeds/image/random",
    "/breed/hound/images",
    "/breed/hound/list",
])
def test_json_schema(base_url, path):
    """Check if json structure is correct"""
    res = requests.get(base_url + f'{path}')

    schema = {
        "type": "object",
        "properties": {
            "message": {},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    validate(instance=res.json(), schema=schema)


@pytest.mark.parametrize("expected_number", [1, 50, 51])
def test_multiple_random_images_response(base_url, expected_number):
    """Check if number of random images in response is correct"""
    response = requests.get(base_url + f"/breeds/image/random/{expected_number}")
    actual_number = len(response.json()["message"])
    if expected_number >= 50:
        assert actual_number == 50
    else:
        assert actual_number == expected_number


@pytest.mark.parametrize("breed", ["hound", "schnauzer", "spaniel"])
def test_random_image_from_breed_collection(base_url, breed):
    """Check if name of random image from breed collection contains breed name"""
    response = requests.get(base_url + f"/breed/{breed}/images/random")
    assert breed in response.json()["message"]
