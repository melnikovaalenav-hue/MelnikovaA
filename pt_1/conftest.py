import pytest
import os
from faker import Faker
from selenium import webdriver
from collections import namedtuple
from selenium.webdriver.chrome.options import Options

fake = Faker()

@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    )
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture
def generate_data():
    login = fake.email()
    password = fake.password()
    NewUser = namedtuple("User", ["login","password"])
    return NewUser(login,password)


