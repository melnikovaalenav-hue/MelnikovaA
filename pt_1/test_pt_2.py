from selenium import webdriver
import pytest
import time

class TestNewUser:
    LOGIN_BUTTON = ("xpath", "//button[@data-testid='enter-another-way']")
    LOGIN_BY_MAIL = ("xpath", "//input[@data-test-id='email-id']")

    @pytest.mark.usefixtures("driver")
    def test_example(self):
        self.driver.get("https://vk.com/")
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    #@pytest.mark.usefixtures("generate_data")
    def test_login(self, generate_data):
        login = generate_data.login
        password = generate_data.password
        print(login, password)








