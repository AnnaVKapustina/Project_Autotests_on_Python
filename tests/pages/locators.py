from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_INNER_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    BASKET_SUM = (By.CSS_SELECTOR, ".alert-info strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert")
