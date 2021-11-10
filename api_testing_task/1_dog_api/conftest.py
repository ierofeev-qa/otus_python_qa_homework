import pytest
import json


@pytest.fixture
def base_url():
    return 'https://dog.ceo/api'


@pytest.fixture
def breeds_list():
    with open("breeds.json", "r") as f:
        breeds = json.loads(f.read())
    return breeds
