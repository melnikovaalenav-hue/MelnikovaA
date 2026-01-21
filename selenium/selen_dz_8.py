import time
from selenium import webdriver

driver = webdriver.Chrome()
#driver.get("https://demoqa.com/checkbox")

#driver.find_element("xpath", "//button[@title='Toggle']").click()
#driver.find_element("xpath", "//span[@class='rct-checkbox']").click()

driver.get("https://demoqa.com/radio-button")

# если чек-бос неактивен
NO = ("xpath", "//input[@id='noRadio']")
#assert driver.find_element(*NO).is_enabled() , "ERROR: NO - is not clickable"

# если используется многослойная реализация
YES_BUTTON = ("xpath", "//input[@id='yesRadio']") # для статуса
YES_LABEL = ("xpath", "//label[@for='yesRadio']") # для взаимодействия

#driver.find_element(*YES_LABEL).click()
#assert driver.find_element(*YES_BUTTON).is_selected()


IMPRESSIVE = ("xpath","//label[@for='impressiveRadio']")
driver.find_element(*IMPRESSIVE).click()

