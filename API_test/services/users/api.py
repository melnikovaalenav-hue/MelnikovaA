import allure
import requests
from API_test.services.users.payloads import Payload
from API_test.config.headers import Headers
from API_test.services.users.endpoints import Endpoints
from API_test.utilis.helper import Helper
from API_test.services.users.models.models_user import UserResponse

class UsersAPI(Helper):

    def __init__(self):
        self.payloads = Payload()
        self.headers = Headers()
        self.endpoints = Endpoints()

    @allure.step("Create user")
    def create_user(self) -> list:
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user()
        )
        return self.validate_response(response, UserResponse)
