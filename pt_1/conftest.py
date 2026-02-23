from collections import namedtuple
import pytest
from faker import Faker
from selenium import webdriver

fake = Faker()

@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture
def generate_data():
    login = fake.email()
    password = fake.password()
    NewUser = namedtuple("User", ["login","password"])
    return NewUser(login,password)


