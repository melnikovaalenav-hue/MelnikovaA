import time
from selenium import webdriver

class TestLogin:

    USERNAME = ("xpath", "//input[@id='userName']")
    PASSWORD = ("xpath", "//input[@id='password']")

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_username_fill_out(self):
        self.driver.get("https://demoqa.com/login")
        self.driver.find_element(*self.USERNAME).send_keys("Alena")
        self.driver.find_element(*self.PASSWORD).send_keys("123")
        upd_username = self.driver.find_element(*self.USERNAME).get_attribute("value")
        upd_password = self.driver.find_element(*self.PASSWORD).get_attribute("value")
        assert upd_username=="Alena" and upd_password == "123", "ERROR, имя другое"
        time.sleep(3)

    def test_box(self):
        self.driver.get("https://demoqa.com/text-box")
        assert self.driver.current_url == "https:", "ERROR, тест не пройдет"
    def teardown_method(self):
        self.driver.quit()

