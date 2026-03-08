from pom.base.base_page import BasePage

class checkout_overview(BasePage):

    PAGE_URL = "https://www.saucedemo.com/checkout-step-two.html"
    PURCHASE = "//button[@id='finish']"

    def order_confirmation(self):
        self.driver.find_element(*self.PURCHASE).click()