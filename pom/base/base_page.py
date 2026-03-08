from pom.metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

    def basket_check(self):
        self.driver.find_element("//div[@id='shopping_cart_container']").click()

    def upd_basket(self, quantity):
        UPD_BASKET = self.driver.find_element("xpath", "//span[@data-test='shopping-cart-badge']").text
        assert UPD_BASKET == quantity, "ERROR, значение не изменилось"

    def url_check(self):
        assert self.driver.current_url == self.PAGE_URL, "ERROR, страница не найдена"

    def page_header(self):
        assert self.driver.title == "Swag Labs", "ERROR, некорректный заголовок"





