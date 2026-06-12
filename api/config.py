import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
