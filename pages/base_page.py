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
