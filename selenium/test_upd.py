from selenium import webdriver

class TestLogin:
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/login")

    def test_password(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/")