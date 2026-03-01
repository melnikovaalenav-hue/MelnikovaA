
from pom.pages.login_page import LoginPage
from pom.base.base_test import BaseTest
import time

class TestLoginPage(BaseTest):

    def test_login_page(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_login()
        time.sleep(3)