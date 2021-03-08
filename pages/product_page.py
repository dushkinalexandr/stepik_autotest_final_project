from .base_page import BasePage
from ..locators import ProductPageLocators
from ..locators import BasketPageLocators
import time

"""
Page Object, который связан со страницей товара.
"""


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def guest_can_see_message_product_add_to_basket(self):
        message_product_add_to_basket = self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT)
        assert message_product_add_to_basket, "Product not add to basket."

    def guest_can_see_same_product_name(self):
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        print(f'Name in store: {product_name_in_store.text}, Name in basket: {product_name_in_basket.text}')
        assert product_name_in_store.text == product_name_in_basket.text, "Product name is no the same"

    def guest_can_see_message_price_basket(self):
        message_price_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BASKET_PRICE)
        assert message_price_basket, "Not see basket price."

    def guest_can_see_correct_price_basket(self):
        product_prise_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_STORE)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        print(f'Price in store: {product_prise_in_store.text}, Price in basket: {product_price_in_basket.text}')
        assert product_prise_in_store.text == product_price_in_basket.text, "Price is wrong"

    def guest_can_add_product_to_basket(self):
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.guest_can_see_message_product_add_to_basket()
        self.guest_can_see_same_product_name()
        self.guest_can_see_message_price_basket()
        self.guest_can_see_correct_price_basket()

