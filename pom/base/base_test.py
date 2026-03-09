from pom.pages.login_page import LoginPage
from pom.pages.catalog_page import AddItemToCart
from pom.pages.product_cart import RemoveProduct
from pom.pages.personal_information_page import PersonalData
from pom.pages.checkout_overview import CheckoutOverview
from pom.pages.checkout_complete import CheckoutComplete


class BaseTest:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.product = AddItemToCart(self.driver)
        self.remov_product = RemoveProduct(self.driver)
        self.personal_information = PersonalData(self.driver)
        self.checkout_overview = CheckoutOverview(self.driver)
        self.checkout_complete = CheckoutComplete(self.driver)






