import time
from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
#options.add_argument("--headless=new")
options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=1200,800")
options.add_argument("--disable-cache")
options.page_load_strategy= 'eager'


driver = webdriver.Chrome(options=options)
driver.get("https://ya.ru/")
##############################################################

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")
file_upload = driver.find_element("xpath", "//input[@id='uploadFile']")
file_upload.send_keys(r"C:\Users\Haden_000\PycharmProjects\MelnikovaA\selenium\files\message.png")

time.sleep(5)




