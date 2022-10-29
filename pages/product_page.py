from .base_page import BasePage
from .locators import ProductPageLocators
import time


#Page Object
class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button_basket.click()
        assert True, "No click button"

    def should_be_success_message_product_is_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == added_product_name, "Added item isn't equal product: {} != '{}'"\
            .format(product_name, added_product_name)

    def should_be_correct_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_total_price = self.browser.find_element(*ProductPageLocators.MESSAGE_CART_PRICE).text
        assert product_price == cart_total_price, "Wrong cart price when added item: {} != {}"\
            .format(product_price, cart_total_price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"


