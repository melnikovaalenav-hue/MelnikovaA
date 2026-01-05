import time
from selenium import webdriver

from selenium.webdriver import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

full_name_input_field = driver.find_element("xpath", "//input[@id='userName']")
full_name_input_field.clear()
assert full_name_input_field.get_attribute("value") == ""
full_name_input_field.send_keys("Alena Mel")

user_email = driver.find_element("xpath", "//input[@id='userEmail']")
user_email.send_keys("moroz.a@mail.com")

user_address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
user_address.send_keys("г.Саратов")

permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanent_address.send_keys("г.Энгельс")

full_name_input_field.send_keys(Keys.CONTROL + "A")
full_name_input_field.send_keys(Keys.BACK_SPACE)

full_name_input_field.send_keys("Den")
assert full_name_input_field.get_attribute("value") == "Den", "Введенные данные не соотвесвтуют ожидаемым"

user_email.send_keys(Keys.CONTROL + "A")
user_email.send_keys(Keys.BACK_SPACE)
assert user_email.get_attribute("value") == "", "Данные не удалены"

user_address.send_keys(Keys.CONTROL + "A")
user_address.send_keys(Keys.DELETE)
assert user_address.get_attribute("value") == "", "Поле не очищено"

permanent_address.send_keys(Keys.CONTROL + "A")
permanent_address.send_keys(Keys.BACKSPACE)
assert permanent_address.get_attribute("value") == ""

time.sleep(5)