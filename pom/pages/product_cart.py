from pom.base.base_page import BasePage

class remove_product(BasePage):

    PAGE_URL = "https://www.saucedemo.com/cart.html"
    REMOVE_PRODUCT_flashlight = "//button[@id='remove-sauce-labs-bike-light']"
    CHECKOUT = "//button[@id='checkout']"

    def remove_flashlight(self):
        self.driver.find_element_by_xpath(self.REMOVE_PRODUCT_flashlight).click()

    def purchase_confirmed(self):
        self.driver.find_element_by_xpath(self.CHECKOUT).click()



