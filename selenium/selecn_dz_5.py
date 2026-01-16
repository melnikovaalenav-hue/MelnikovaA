from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")
wath = WebDriverWait(driver, 7, poll_frequency=1)

button_activation = ("xpath", "//button[@id='enableAfter']")

wath.until(EC.element_to_be_clickable(button_activation)).click()
wath.until(EC.visibility_of_element_located(button_activation))
wath.until(EC.text_to_be_present_in_element(button_activation, "Will enable 5 seconds"))