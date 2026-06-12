import requests

from api.config import BASE_URL


class PostAPI:

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get_posts(self):
        return requests.get(f"{self.base_url}/posts")

    def get_post(self, post_id):
        return requests.get(f"{self.base_url}/posts/{post_id}")

    def get_posts_by_user(self, user_id):
        return requests.get(f"{self.base_url}/posts", params={"userId": user_id})
