from collections import namedtuple
import pytest
from faker import Faker
from selenium import webdriver

fake = Faker()

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver

@pytest.fixture
def generate_data():
    Login = fake.email()
    password = fake.password()
    NewUser = namedtuple("User", ["login","password"])
    return NewUser(Login,password)


