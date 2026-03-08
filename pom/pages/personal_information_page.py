from pom.base.base_page import BasePage

class personal_data(BasePage):

    PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    FIRST_NAME = "//input[@id='first-name']"
    LAST_NAME = "//input[@id='last-name']"
    POSTAL_CODE = "//input[@id='postal-code']"
    CONTINUE = "//input[@id='continue']"

    def fill_in_personal_data(self):
        first_name_upd = self.driver.find_element(*self.FIRST_NAME)
        first_name_upd.clear()
        first_name_upd.send_keys("Petrov")

        last_name_upd = self.driver.find_element(*self.LAST_NAME)
        last_name_upd.clear()
        last_name_upd.send_keys("Petrov")

        postal_code_upd = self.driver.find_element(*self.POSTAL_CODE)
        postal_code_upd.clear()
        postal_code_upd.send_keys("123456")

        first_name_upd.get_attribute("value")
        last_name_upd.get_attribute("value")
        assert first_name_upd == "Petrov", "ERROR, Сохраненное в поле Фамилия значение - не соотвествует добавленному"
        assert last_name_upd == "Ivan", "ERROR, Сохраненное в поле Имя значение - не соотвествует добвленному"

        self.driver.find_element(*self.CONTINUE).click()

