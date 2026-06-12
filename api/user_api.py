import requests

from api.config import BASE_URL


class UserAPI:

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get_users(self):
        return requests.get(f"{self.base_url}/users")

    def get_user(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}")

    def create_user(self, data):
        return requests.post(f"{self.base_url}/users", json=data)

    def update_user(self, user_id, data):
        return requests.put(f"{self.base_url}/users/{user_id}", json=data)

    def delete_user(self, user_id):
        return requests.delete(f"{self.base_url}/users/{user_id}")

    def get_user_posts(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}/posts")
