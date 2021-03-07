from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE_IN_STORE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div:first-child strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")


class BasketPageLocators():
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-4 > h3 > a")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset > div > div > div:nth-child(5) > p")

