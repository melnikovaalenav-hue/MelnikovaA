import json
from selenium.webdriver.chrome.webdriver import WebDriver

class CookieManager:
    def __init__(self, driver,fail_path="cookie.json"):
        self.driver = driver
        self.fail_path: WebDriver = fail_path
    def save_cookie(self):
        cookies = self.driver.get_cookies()
        with open(self.fail_path, "w") as file:
            json.dump(cookies, file, indent=4)
    def load_cookie(self):
        self.driver.delete_all_cookies()
        with open(self.fail_path, "r") as file:
            cookies = self.driver.get_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

