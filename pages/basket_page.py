from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_is_cart_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Item is presented, but should not be"

    def check_is_cart_empty_message(self):
        basket_empty_message = (self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)).text
        assert "Your basket is empty." in basket_empty_message, \
            "Empty message wrong"
