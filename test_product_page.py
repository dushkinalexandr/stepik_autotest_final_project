import pytest
from .pages.product_page import ProductPage
import time

URL_PRODUCT_NewYear = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]

# URL_PRODUCT = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

"""
xfile - номер страницы, на которой тест падает с ошибкой "AssertionError: Product name is no the same"
mask - шаблон URL
links - с помощью генератора формируем список урлов для параметризации теста, исключая ошибочный
xlink - ошибочный урл с доп.параметром с отметкой XFAIL (ожидаемо падает)
вставляем в список links ошибочный урл xlink на место xfile
"""
xfile = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [mask+str(i) for i in range(10) if i != xfile]
xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
links.insert(xfile, xlink)


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    # time.sleep(30)


@pytest.mark.parametrize('link', URL_PRODUCT_NewYear)
def test_guest_can_add_product_to_basket_promo_newyear(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()


def test_guest_can_add_product_to_basket_without_promo(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.guest_can_see_message_product_add_to_basket()
    page.guest_can_see_same_product_name()
    page.guest_can_see_message_price_basket()
    page.guest_can_see_correct_price_basket()


# def test_guest_check_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()

