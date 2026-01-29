import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

DROPDOWN_ELEMENT = ("xpath", "//select[@id='oldSelectMenu']")

DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
#DROPDOWN.select_by_visible_text("Yellow") # поиск по тексту
#DROPDOWN.select_by_index(10) # поиск по индексу
DROPDOWN.select_by_value("5")

time.sleep(2)

#-----
from selenium.webdriver import Keys

MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")
select = driver.find_element(*MULTISELECT)
select.send_keys("Blue")
select.send_keys(Keys.ENTER)
select.send_keys("Green")
green_check = driver.find_element(*MULTISELECT).get_attribute("value")
assert "Green" in green_check, "ERROR Green is null"

time.sleep(2)

