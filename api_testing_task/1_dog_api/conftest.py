import pytest
import json
import os


@pytest.fixture
def base_url():
    return 'https://dog.ceo/api'


@pytest.fixture
def breeds_list():
    script_dir = os.path.dirname(__file__)
    rel_path = "breeds.json"
    with open(os.path.join(script_dir, rel_path), "r", encoding='UTF-8') as f:
        breeds = json.loads(f.read())
    return breeds
