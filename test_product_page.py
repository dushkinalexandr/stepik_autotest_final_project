import pytest
from .pages.product_page import ProductPage
import time

URL_PRODUCT = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('url', URL_PRODUCT)
def test_guest_can_add_product_to_basket(browser, url):
    link = url
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    # time.sleep(30)


# def test_guest_check_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()

