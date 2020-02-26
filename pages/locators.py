from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ADDED_TO_BASKET_SUCCESS = (By.CSS_SELECTOR, "#messages div.alert-success")
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, "div.alert-success div.alertinner strong")
    PRICE_OF_THE_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages div.alert-info div.alertinner strong")
