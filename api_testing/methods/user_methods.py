import allure
import requests
from api_testing.data import base_url, create_user_endpoint, login_user_endpoint, delete_user_endpoint, \
    update_user_endpoint


class UserMethods:
    @allure.step('Создание пользователя через POST-запрос.')
    def create_user(self, payload):
        method_url = f"{base_url}{create_user_endpoint}"
        response = requests.post(url = method_url, data = payload)
        return response

    @allure.step('Логин пользователя через POST-запрос.')
    def login_user(self, payload):
        method_url = f"{base_url}{login_user_endpoint}"
        response = requests.post(url = method_url, data = payload)
        return response

    @allure.step('Удаление пользователя через DELETE-запрос.')
    def delete_user(self, access_token):
        method_url = f"{base_url}{delete_user_endpoint}"
        headers = {"authorization": access_token}
        response = requests.delete(url = method_url, headers = headers)
        return response

    @allure.step('Обновление данных пользователя через PATCH-запрос.')
    def update_user_data(self, access_token, payload):
        method_url = f"{base_url}{update_user_endpoint}"
        headers = {"authorization": access_token}
        response = requests.patch(url = method_url, headers = headers, data = payload)
        return response