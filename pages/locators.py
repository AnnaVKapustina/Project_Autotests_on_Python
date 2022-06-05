from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_IN_HEADER = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_INNER_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    BASKET_SUM = (By.CSS_SELECTOR, ".alert-info strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert")


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
