import pytest


@pytest.mark.regression
@pytest.mark.parametrize("user_id,expected_status", [(999, 404), (0, 404)])
def test_get_user_not_found(user_api, user_id, expected_status):
    response = user_api.get_user(user_id)
    assert response.status_code == expected_status


@pytest.mark.regression
def test_get_user_invalid_id(user_api):
    response = user_api.get_user("abc")
    assert response.status_code == 404
