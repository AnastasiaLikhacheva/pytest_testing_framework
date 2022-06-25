from allure import step
from api.base_api import BaseApi


class ApiOzon(BaseApi):
    @step('POST-запрос. Добавление в корзину. URL: https://www.ozon.ru/api/composer-api.bx/_action/addToCart')
    def ozon_post(self, data):
        return self.send_post(url='/composer-api.bx/_action/addToCart', data=data)
