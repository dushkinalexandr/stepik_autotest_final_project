from .base_page import BasePage
# точка в импорте
# ImportError: attempted relative import with no known parent package
from selenium.webdriver.common.by import By

"""
Page Object, который будет связан с главной страницей интернет-магазина.
"""


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

