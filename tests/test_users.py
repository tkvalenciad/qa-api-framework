import pytest


@pytest.mark.smoke
def test_get_users(user_api):
    response = user_api.get_users()
    assert response.status_code == 200


@pytest.mark.regression
def test_users_response_contains_data(users_list):
    assert "id" in users_list[0]
    assert "name" in users_list[0]
    assert "email" in users_list[0]


@pytest.mark.smoke
def test_get_user_by_id(user_api):
    response = user_api.get_user(1)
    body = response.json()

    assert response.status_code == 200
    assert body["id"] == 1
    assert body["name"]
    assert body["email"]


@pytest.mark.regression
def test_get_users_returns_ten_users(users_list):
    assert len(users_list) == 10


@pytest.mark.regression
def test_users_have_unique_ids(users_list):
    ids = [user["id"] for user in users_list]
    assert len(ids) == len(set(ids))


@pytest.mark.regression
def test_user_email_format(users_list):
    for user in users_list:
        assert "@" in user["email"]


@pytest.mark.regression
def test_user_has_nested_address_and_company(user_api):
    body = user_api.get_user(1).json()

    assert "street" in body["address"]
    assert "name" in body["company"]


@pytest.mark.regression
@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_user_by_id_parametrized(user_api, user_id):
    response = user_api.get_user(user_id)
    assert response.status_code == 200
    assert response.json()["id"] == user_id


@pytest.mark.regression
def test_create_user(user_api):
    payload = {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com",
    }
    response = user_api.create_user(payload)
    body = response.json()

    assert response.status_code == 201
    assert body["name"] == payload["name"]
    assert body["email"] == payload["email"]
    assert "id" in body


@pytest.mark.regression
def test_update_user(user_api):
    payload = {"name": "Updated Name", "email": "updated@example.com"}
    response = user_api.update_user(1, payload)
    body = response.json()

    assert response.status_code == 200
    assert body["name"] == payload["name"]
    assert body["email"] == payload["email"]


@pytest.mark.regression
def test_delete_user(user_api):
    response = user_api.delete_user(1)
    assert response.status_code == 200


@pytest.mark.regression
def test_get_user_posts(user_api):
    response = user_api.get_user_posts(1)
    posts = response.json()

    assert response.status_code == 200
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)
