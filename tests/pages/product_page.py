from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        cart_button.click()
        self.solve_quiz_and_get_code()

    def should_be_book_name(self):
        book_name = (self.browser.find_element(*ProductPageLocators.BOOK_NAME)).text
        book_name_inner = (self.browser.find_element(*ProductPageLocators.ALERT_INNER_BOOK_NAME)).text
        assert book_name == book_name_inner, "Book name is not excepted in alert"

    def should_be_cart_sum(self):
        book_price = (self.browser.find_element(*ProductPageLocators.BOOK_PRICE)).text
        cart_sum = (self.browser.find_element(*ProductPageLocators.BASKET_SUM)).text
        assert book_price == cart_sum, "Sum cart != book price"
