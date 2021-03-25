from .base_page import BasePage
from ..locators import MainPageLocators
from ..locators import BasketPageLocators

# точка в импорте
# ImportError: attempted relative import with no known parent package

"""
Page Object, который связан с главной страницей интернет-магазина.
"""


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def guest_can_see_message_basket_is_empty(self):
        # Checking the display of the message
        message = "Your basket is empty."
        message_basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert message in message_basket_empty.text, "Basket not empty."
