from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..locators import MainPageLocators

# точка в импорте
# ImportError: attempted relative import with no known parent package

"""
Page Object, который будет связан с главной страницей интернет-магазина.
"""


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
