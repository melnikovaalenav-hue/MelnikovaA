from pom.base.base_page import BasePage

class add_item_to_cart(BasePage):

    PAGE_URL = "https://www.saucedemo.com/inventory.html"
    PRODUCT_backpack = "//button[@id='add-to-cart-sauce-labs-backpack']"
    PRODUCT_flashlight = "//button[@id='add-to-cart-sauce-labs-bike-light']"

    def product_selection(self):
        self.driver.find_element(*self.PRODUCT_backpack).click()
        self.driver.find_element(*self.PRODUCT_flashlight).click()