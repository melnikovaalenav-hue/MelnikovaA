from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pom.metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

