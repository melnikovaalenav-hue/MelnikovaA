from pom.base.base_page import BasePage

class LoginPage(BasePage):

    PAGE_URL = "https://www.saucedemo.com"
    LOGIN_FIELD =  "//input[@id='user-name']"
    PASSWORD_FIELD = "//input[@id='password']"
    LOGIN_SUBMIT_BUTTON ="//input[@id='login-button']"

    def enter_login(self):
        self.driver.find_element(*self.LOGIN_FIELD).send_keys("standard_user")

    def enter_password(self):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("secret_sauce")

    def click_login(self):
        self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON).click()



