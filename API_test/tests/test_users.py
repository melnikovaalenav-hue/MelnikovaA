from API_test.config.base_test import BaseTest

class TestUsers(BaseTest):

    def test_create_user(self):
        user = self.users_api.create_user()
        print(user)