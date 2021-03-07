from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


# def test_guest_should_see_login_url(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page_form = LoginPage(browser, link)
#     page_form.open()
#     page_form.should_be_login_url()
#
#
# def test_guest_should_see_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page_form = LoginPage(browser, link)
#     page_form.open()
#     page_form.should_be_login_form()
#
#
# def test_guest_should_see_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page_form = LoginPage(browser, link)
#     page_form.open()
#     page_form.should_be_register_form()



