from .base_page import BasePage
from ..locators import BasketPageLocators


"""
Page Object, which is linked to the basket page.
"""


class BasketPage(BasePage):
    def guest_can_see_message_basket_is_empty(self):
        # Checking the display of the message
        message_basket_empty = self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert message_basket_empty == "Your basket is empty.", "Basket not empty."
