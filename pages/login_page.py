from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, "'login' is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_2)
        password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
