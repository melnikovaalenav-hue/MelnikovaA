from pom.metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    BASKET = "//div[@id='shopping_cart_container']"
    UPD_BASKET = "//div[@id='shopping_cart_container']"


    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

    def basket_check(self):
        self.driver.find_element(*self.BASKET).click()

    def upd_basket(self, quantity):
        UPD_BASKET = self.driver.find_element(*self.UPD_BASKET).text
        assert UPD_BASKET == quantity, "ERROR, значение не изменилось"

    def url_check(self):
        assert self.driver.current_url == self.PAGE_URL, "ERROR, страница не найдена"

    def page_header(self):
        assert self.driver.title == "Swag Labs", "ERROR, некорректный заголовок"





