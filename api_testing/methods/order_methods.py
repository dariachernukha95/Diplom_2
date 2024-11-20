import allure
import requests
from api_testing.data import base_url, order_endpoint


class OrderMethods:

    @allure.step('Создание заказа через POST-запрос.')
    def create_order(self, access_token, ingredients_list):
        method_url = f"{base_url}{order_endpoint}"
        payload = {"ingredients": ingredients_list}
        headers = {"authorization": access_token}
        response = requests.post(url = method_url, headers =  headers, data = payload)
        return response

    @allure.step('Получение заказов пользователя через GET-запрос.')
    def get_order(self, access_token):
        method_url = f"{base_url}{order_endpoint}"
        headers = {"authorization": access_token}
        response = requests.get(url=method_url, headers=headers)
        return response