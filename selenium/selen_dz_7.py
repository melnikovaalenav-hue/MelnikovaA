import time
import os.path
from selenium import webdriver
from selen_dz_7_1 import CookieManager

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")

login = ("xpath", "//input[@id='login_email']")
password = ("xpath", "//input[@id='password']")
button = ("xpath", "//button[@id='loginformsubmit']")

cookiesManager = CookieManager(driver)

if os.path.exists("cookie.json"):
    cookie_manager.load()
else:
    driver.find_element(*login).send_keys("morosowa.a@yandex.ru")
    driver.find_element(*password).send_keys("0891528011Alena-")
    driver.find_element(*button).click()
    cookiesManager.save_cookie()

time.sleep(5)