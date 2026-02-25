import pytest
import allure
import time
from allure_commons.types import Severity
from allure_commons.types import AttachmentType


@allure.epic("Purchase")
@allure.feature("Adding an item to your cart")
@allure.story("Payment for the order")
class TestPurchaseOfGoods:

    @pytest.mark.smoke
    @allure.title("Purchase of goods")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="TZ")

    def test_purchase(self):
        with allure.step("Open page. Step 1"):
            self.driver.get("https://www.saucedemo.com")
            LOGIN = self.driver.find_element("xpath", "//input[@id='user-name']")
            PASSWORD = self.driver.find_element("xpath", "//input[@id='password']")
            LOGIN_BUTTON = self.driver.find_element("xpath", "//input[@id='login-button']")

            LOGIN.send_keys("standard_user")
            PASSWORD.send_keys("secret_sauce")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Open page",
                attachment_type=allure.attachment_type.PNG
            )
            LOGIN_BUTTON.click()

        # assert driver.current_url == "https://www.saucedemo.com/inventory.html", "ERROR, страница не найдена"
        with allure.step("The correct page has been opened. Step 2"):
            assert self.driver.title == "Swag Labs", "ERROR, некорректный заголовок"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="The correct page has been opened",
                attachment_type=allure.attachment_type.PNG
                )

        with allure.step("Add item to cart. Step 3"):
            PRODUCT_backpack = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
            PRODUCT_flashlight = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
            BASKET = self.driver.find_element("xpath", "//div[@id='shopping_cart_container']")

            PRODUCT_backpack.click()
            PRODUCT_flashlight.click()
            BASKET.click()
        with allure.step("Make sure the basket is open. Step 4"):
            assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "ERROR, страница не найдена"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Product added to cart",
                attachment_type=allure.attachment_type.PNG
                )

        with allure.step("Remove item from cart. Step 5"):
            REMOVE_PRODUCT_flashlight = self.driver.find_element("xpath", "//button[@id='remove-sauce-labs-bike-light']")
            REMOVE_PRODUCT_flashlight.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Product removed",
                attachment_type=allure.attachment_type.PNG
                )
        with allure.step("Product removed. Step 6"):
            UPD_BASKET = self.driver.find_element("xpath", "//span[@data-test='shopping-cart-badge']").text
            assert UPD_BASKET == "1", "ERROR, значение не изменилось"

        with allure.step("Go to the page for filling in personal data. Step 7"):
            CHECKOUT = self.driver.find_element("xpath", "//button[@id='checkout']")
            CHECKOUT.click()
        with allure.step("The page for filling in data is open. Step 8"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

        with allure.step("Filling out personal data. Step 9"):
            FIRST_NAME = self.driver.find_element("xpath", "//input[@id='first-name']")
            LAST_NAME = self.driver.find_element("xpath", "//input[@id='last-name']")
            POSTAL_CODE = self.driver.find_element("xpath", "//input[@id='postal-code']")

            FIRST_NAME.send_keys("Petrov")
            LAST_NAME.send_keys("Ivan")
            POSTAL_CODE.send_keys("123456")

        with allure.step("The data is filled in correctly. Step 10"):
            UPD_FIRST_NAME = self.driver.find_element("xpath", "//input[@id='first-name']").get_attribute("value")
            UPD_LAST_NAME = self.driver.find_element("xpath", "//input[@id='last-name']").get_attribute("value")
            assert UPD_FIRST_NAME == "Petrov", "ERROR, Сохраненное в поле Фамилия значение - не соотвествует добавленному"
            assert UPD_LAST_NAME == "Ivan", "ERROR, Сохраненное в поле Имя значение - не соотвествует добвленному"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Data is correct",
                attachment_type=allure.attachment_type.PNG
                )

        with allure.step("Checkout Overview. Step 11"):
            CONTINUE = self.driver.find_element("xpath", "//input[@id='continue']")
            CONTINUE.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Checkout Overview",
                attachment_type=allure.attachment_type.PNG
                )
        with allure.step("Assert open page. Step 12"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "ERROR, Страница не найдена"

        with allure.step("Order confirmation. Step 13"):
            PURCHASE = self.driver.find_element("xpath", "//button[@id='finish']")
            PURCHASE.click()

        with allure.step("Order created successfully. Step 13"):
            Confirmation_message = self.driver.find_element("xpath", "//h2[@data-test='complete-header']").text
            assert (self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
                and Confirmation_message == "Thank you for your order!"), "ERROR, Что-то пошло не по плану"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Order created successfully",
                attachment_type=allure.attachment_type.PNG
                )

        time.sleep(2)