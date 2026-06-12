import pytest

from api.post_api import PostAPI
from api.user_api import UserAPI


@pytest.fixture
def user_api():
    return UserAPI()


@pytest.fixture
def post_api():
    return PostAPI()


@pytest.fixture
def users_list(user_api):
    response = user_api.get_users()
    assert response.status_code == 200
    return response.json()
