from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        cart_button.click()
        self.solve_quiz_and_get_code()

    def should_be_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME) \
               == self.is_element_present(*ProductPageLocators.ALERT_INNER_BOOK_NAME), \
            "Book name is not excepted in alert"

    def should_be_cart_sum(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE) \
               == self.is_element_present(*ProductPageLocators.BASKET_SUM), \
            "Sum cart != book price"
