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

PRODUCT_backpack = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
PRODUCT_flashlight = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
BASKET = driver.find_element("xpath", "//div[@id='shopping_cart_container']")

PRODUCT_backpack.click()
PRODUCT_flashlight.click()
BASKET.click()
assert driver.current_url == "https://www.saucedemo.com/cart.html", "ERROR, страница не найдена"

REMOVE_PRODUCT_flashlight = driver.find_element("xpath", "//button[@id='remove-sauce-labs-bike-light']")
REMOVE_PRODUCT_flashlight.click()

UPD_BASKET = driver.find_element("xpath","//span[@data-test='shopping-cart-badge']").text
assert UPD_BASKET == "1", "ERROR, значение не изменилось"

CHECKOUT = driver.find_element("xpath", "//button[@id='checkout']")
CHECKOUT.click()
assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

FIRST_NAME = driver.find_element("xpath", "//input[@id='first-name']")
LAST_NAME = driver.find_element("xpath", "//input[@id='last-name']")
POSTAL_CODE = driver.find_element("xpath", "//input[@id='postal-code']")

FIRST_NAME.send_keys("Petrov")
LAST_NAME.send_keys("Ivan")
POSTAL_CODE.send_keys("123456")

UPD_FIRST_NAME = driver.find_element("xpath", "//input[@id='first-name']").get_attribute("value")
UPD_LAST_NAME = driver.find_element("xpath", "//input[@id='last-name']").get_attribute("value")
assert UPD_FIRST_NAME == "Petrov", "ERROR, Сохраненное в поле Фамилия значение - не соотвествует добавленному"
assert UPD_LAST_NAME == "Ivan", "ERROR, Сохраненное в поле Имя значение - не соотвествует добвленному"

CONTINUE = driver.find_element("xpath", "//input[@id='continue']")
CONTINUE.click()
assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "ERROR, Страница не найдена"

PURCHASE = driver.find_element("xpath", "//button[@id='finish']")
PURCHASE.click()
Confirmation_message = driver.find_element("xpath","//h2[@data-test='complete-header']").text
assert (driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
        and Confirmation_message == "Thank you for your order!"), "ERROR, Что-то пошло не по плану"

time.sleep(2)