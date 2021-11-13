import pytest
import requests


@pytest.mark.parametrize("path", [
    "/posts",
    "/posts/1",
    "/posts/1/comments",
    "/comments?postId=1"
])
def test_status_code(base_url, path):
    """Check page status code"""
    assert requests.get(base_url + f"{path}").status_code == 200


@pytest.mark.parametrize("path, expected_number", [
    ("/posts", 100),
    ("/comments", 500),
    ("/albums", 100),
    ("/photos", 5000),
    ("/todos", 200),
    ("/users", 10)
])
def test_number_of_returned_items(base_url, path, expected_number):
    """Check that amount of returned items is equal to the etalon"""
    response = requests.get(base_url + f"{path}")
    actual_number = len(response.json())
    assert actual_number == expected_number


def test_post_method(base_url):
    """Check POST method on resource"""
    data = {
        "title": "test_title",
        "body": "test_body",
        "userId": 1
    }

    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    response = requests.post(
        base_url + '/posts',
        headers=headers,
        json=data
    )

    assert response.status_code == 201


def test_put_method(base_url):
    """Check POST method on resource"""
    data = {
        "title": "test_title",
        "body": "test_body",
        "userId": 1
    }

    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    response = requests.put(
        base_url + '/posts/1',
        headers=headers,
        json=data
    )

    assert response.status_code == 200


def test_delete_method(base_url):
    """Check DELETE method on resource"""
    data = {
        "title": "test_title",
        "body": "test_body",
        "userId": 1
    }

    requests.post(
        base_url + '/posts/1',
        json=data
    )

    response = requests.delete(base_url + '/posts/1', json=data)

    assert response.status_code == 200
