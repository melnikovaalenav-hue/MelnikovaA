from pom.pages.login_page import LoginPage
from pom.base.base_test import BaseTest
import allure
import time


class TestPurchaseOfGoods(BaseTest):

    @allure.epic("Purchase")
    @allure.feature("Adding an item to your cart")
    @allure.story("Payment for the order")

    def test_purchase(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_login()
        self.login_page.page_header()
        self.product.product_selection()
        self.login_page.basket_check()
        self.remov_product.url_check()
        self.login_page.upd_basket("2")
        self.remov_product.remove_flashlight()
        self.login_page.upd_basket("1")
        self.remov_product.purchase_confirmed()
        self.personal_information.fill_in_personal_data()
        self.checkout_overview.url_check_checkout_overview()
        self.checkout_overview.order_confirmation()
        self.checkout_complete.the_order_has_been_placed()
        time.sleep(3)