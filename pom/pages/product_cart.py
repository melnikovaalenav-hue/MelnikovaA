from pom.base.base_page import BasePage

class RemoveProduct(BasePage):

    PAGE_URL = "https://www.saucedemo.com/cart.html"
    REMOVE_PRODUCT_flashlight = "//button[@id='remove-sauce-labs-bike-light']"
    CHECKOUT = "//button[@id='checkout']"

    def remove_flashlight(self):
        self.driver.find_element(*self.REMOVE_PRODUCT_flashlight).click()

    def purchase_confirmed(self):
        self.driver.find_element(*self.CHECKOUT).click()



