import time
from multiprocessing.connection import address_type
from urllib.request import URLopener

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")

LOGIN = driver.find_element("xpath", "//input[@id='user-name']")
PASSWORD = driver.find_element("xpath", "//input[@id='password']")
LOGIN_BUTTON = driver.find_element("xpath", "//input[@id='login-button']")

LOGIN.send_keys("standard_user")
PASSWORD.send_keys("secret_sauce")
LOGIN_BUTTON.click()

#assert driver.current_url == "https://www.saucedemo.com/inventory.html", "ERROR, страница не найдена"

assert driver.title == "Swag Labs", "ERROR, некорректный заголовок"
time.sleep(2)