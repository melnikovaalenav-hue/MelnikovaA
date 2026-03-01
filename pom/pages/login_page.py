from pom.base.base_page import BasePage

class LoginPage(BasePage):

    PAGE_URL = "https://www.freeconferencecall.com/ru/ru/login"
    LOGIN_FIELD =  "//input[@id='login_email']"
    PASSWORD_FIELD = "//input[@id='password']"
    LOGIN_SUBMIT_BUTTON ="//button[@id='loginformsubmit']"

    def enter_login(self):
        self.driver.find_element(*self.LOGIN_FIELD).send_keys("WERT@mail.com")

    def enter_password(self):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("qwerty")

    def click_login(self):
        self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON).click()



