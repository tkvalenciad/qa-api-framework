import requests


class UserAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_users(self):
        return requests.get(f"{self.BASE_URL}/users")