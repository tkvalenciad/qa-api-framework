from api.user_api import UserAPI


def test_get_users():

    api = UserAPI()

    response = api.get_users()

    assert response.status_code == 200