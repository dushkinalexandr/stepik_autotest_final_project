from .base_page import BasePage
from ..locators import ProductPageLocators
from ..locators import BasketPageLocators
import time

"""
Page Object, который связан со страницей товара.
"""


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def guest_can_see_product_name(self):
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        print(f'Name in store: {product_name_in_store}, Name in basket: {product_name_in_basket}')
        assert product_name_in_store.text == product_name_in_basket.text, "Product name is no the same"

    def product_price_is_correct(self):
        product_prise_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_STORE)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        print(f'Price in store: {product_prise_in_store}, Price in basket: {product_price_in_basket}')
        assert product_prise_in_store.text == product_price_in_basket.text, "Price is wrong"

