from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_PAGE), \
            "Basket is not empty, but should be"

    def should_be_empty_message(self):
        empty_message = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY).text
        assert "Your basket is empty." in empty_message, "Basket is not empty message, but should be"
