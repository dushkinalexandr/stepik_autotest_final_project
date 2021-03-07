from .base_page import BasePage
from ..locators import ProductPageLocators

"""
Page Object, который связан с главной страницей интернет-магазина.
"""


class BasketPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    # def should_be_login_link(self):
    #     assert self.is_element_present(*BasketPageLocators.LOGIN_LINK), "Login link is not presented"
    #     # символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
