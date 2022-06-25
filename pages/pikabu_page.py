from core.utils.allure_wrapper import step
from core.utils.selene import have
from elements.elements import Elements
from elements.selectors import H3


class PikabuPage(Elements):
    def __init__(self, browser):
        self.browser = browser

    @step('Открытие страницы Pikabu')
    def open(self, url='/'):
        self.browser.open(url)

    @step('Открытие раздела')
    def click_chapter_best(self):
        self.element("//*[a='Лучшее']//a[@href]").press_enter()

    @step('Поиск текста: {title}')
    def search_text(self, title):
        self.element(H3).should(have.text(title))
