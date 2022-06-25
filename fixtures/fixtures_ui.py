import pytest

from pages import GooglePage, PikabuPage


@pytest.fixture(scope='function')
def google_page(browser):
    return GooglePage(browser)


@pytest.fixture(scope='function')
def pikabu_page(browser):
    return PikabuPage(browser)
