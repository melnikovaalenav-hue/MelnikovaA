from pom.base.base_page import BasePage

class PersonalData(BasePage):

    PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    FIRST_NAME = "//input[@id='first-name']"
    LAST_NAME = "//input[@id='last-name']"
    POSTAL_CODE = "//input[@id='postal-code']"
    CONTINUE = "//input[@id='continue']"

    def fill_in_personal_data(self):
        first_name = self.driver.find_element(*self.FIRST_NAME)
        first_name.clear()
        first_name.send_keys("Petrov")

        last_name = self.driver.find_element(*self.LAST_NAME)
        last_name.clear()
        last_name.send_keys("Ivan")

        postal_code = self.driver.find_element(*self.POSTAL_CODE)
        postal_code.clear()
        postal_code.send_keys("123456")

        first_name_upd = first_name.get_attribute("value")
        last_name_upd = last_name.get_attribute("value")
        assert first_name_upd == "Petrov", "ERROR, Сохраненное в поле Фамилия значение - не соотвествует добавленному"
        assert last_name_upd == "Ivan", "ERROR, Сохраненное в поле Имя значение - не соотвествует добвленному"

        self.driver.find_element(*self.CONTINUE).click()

