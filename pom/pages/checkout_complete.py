from pom.base.base_page import BasePage

class checkout_complete(BasePage):

    PAGE_URL = "https://www.saucedemo.com/checkout-complete.html"

    def the_order_has_been_placed(self):
        confirmation_message = self.driver.find_element("//h2[@data-test='complete-header']").text

        assert (self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
                and confirmation_message == "Thank you for your order!"), "ERROR, Что-то пошло не по плану"
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Order created successfully",
            attachment_type=allure.attachment_type.PNG
        )
