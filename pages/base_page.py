from selenium.common.exceptions import NoSuchElementException
"""
Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы.
В ней мы опишем вспомогательные методы для работы с драйвером.
"""


class BasePage():
    def __init__(self, browser, url, timeout=10):
        # конструктор — метод, который вызывается, когда мы создаем объект
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        :param how:  - как искать (css, id, xpath)
        :param what: - что искать (строка-селектор)
        :return:
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
