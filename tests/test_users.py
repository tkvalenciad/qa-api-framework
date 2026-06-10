import pytest
from api.user_api import UserAPI


@pytest.mark.smoke
def test_get_users():

    api = UserAPI()

    response = api.get_users()

    assert response.status_code == 200

@pytest.mark.regression
def test_users_response_contains_data():

    api = UserAPI()

    response = api.get_users()

    body = response.json()

    assert "id" in body[0]
    assert "name" in body[0]
    assert "email" in body[0]