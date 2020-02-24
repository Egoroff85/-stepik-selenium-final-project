from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_in_the_basket(self):
        success_message = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_SUCCESS)
        assert success_message.is_displayed(), "No success message visible"

    def should_be_proper_product_name_in_the_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_added_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED).text
        assert product_name == product_name_added_to_basket, "Product name in the basket is wrong"

    def should_be_proper_product_price_in_the_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_added_to_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT_ADDED).text
        assert price == price_added_to_basket, "Price of the product in the basket is wrong"
