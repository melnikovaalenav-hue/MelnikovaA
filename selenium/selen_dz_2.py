import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://hyperskill.org")
time.sleep(2)

url = driver.current_url
print(url)

if "Login" in url:
    print(f"Страница открыта корректно")
else:
    print(f"Некорректный пеереход на страницу авторизации")
############################################################
if "https://hyperskill.org" in url:
    print(f"Страница открыта корректная")
else:
    print(f"url не совпадает с О.Р")
############################################################
assert driver.current_url == "https://hyperskill.org/", "Ошибка url не совпадает"
############################################################

title = driver.title
print(title)

assert "Hyperskill - Learn to code and break into tech" == title, "Заголовок не совпадает"


