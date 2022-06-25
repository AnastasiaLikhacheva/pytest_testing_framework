from allure import title, description, suite, parent_suite

from data.ozon.request import POST_REQUEST_CART_SUCCESS
from data.ozon.response import POST_RESPONSE_CART_SUCCESS
from helpers.utils import asserts


@parent_suite('[Pytest][API]')
@suite('Ozon')
class TestApiOzon:
    @title('Ozon: Добавление в корзину')
    @description('Добавление в корзину. POST: /composer-api.bx/_action/addToCart')
    def test_api_ozon_get(self, api_ozon):
        asserts(
            # в actual_data записывается то, что вернет сервер
            actual_data=api_ozon.ozon_post(POST_REQUEST_CART_SUCCESS),
            # в asserts_data записывается то, что мы подготовили или ожидаем
            asserts_data=POST_RESPONSE_CART_SUCCESS
        )
