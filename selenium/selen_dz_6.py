import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:142.0) Gecko/20100101 Firefox/142.0")
options.page_load_strategy='eager' # не дожидаемся полной загрузки всех ресурсов


driver = webdriver.Chrome(options=options)
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")

################################################

driver.get("https://demoqa.com/alerts")
driver.find_element("xpath", "//button[@id='alertButton']").click()
driver.switch_to.alert.accept()

wait = WebDriverWait(driver, 10,poll_frequency=1)

driver.find_element("xpath", "//button[@id='timerAlertButton']").click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()

driver.find_element("xpath", "//button[@id='confirmButton']").click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.dismiss()

driver.find_element("xpath", "//button[@id='promtButton']").click()
alert = wait.until(EC.alert_is_present())
alert.send_keys("Alena")
alert.accept()

time.sleep(5)

