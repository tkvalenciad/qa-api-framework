import pytest


@pytest.mark.smoke
def test_get_posts(post_api):
    response = post_api.get_posts()
    assert response.status_code == 200


@pytest.mark.regression
def test_get_posts_returns_hundred_posts(post_api):
    posts = post_api.get_posts().json()
    assert len(posts) == 100


@pytest.mark.smoke
def test_get_post_by_id(post_api):
    response = post_api.get_post(1)
    body = response.json()

    assert response.status_code == 200
    assert body["id"] == 1
    assert body["title"]
    assert body["body"]


@pytest.mark.regression
def test_get_posts_by_user(post_api):
    posts = post_api.get_posts_by_user(1).json()

    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)


@pytest.mark.regression
def test_get_post_not_found(post_api):
    response = post_api.get_post(999)
    assert response.status_code == 404
