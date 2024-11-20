import allure
import pytest

from api_testing.data import error_of_authorization_response
from api_testing.methods.user_methods import UserMethods

class TestUserUpdate():

    @allure.title('Проверка возможности обновления данных авторизованного пользователя.')
    @pytest.mark.parametrize('field, value', [
        ("email", "dchernukha27@mail.ru"),
        ("password", "1234567"),
        ("name", "Darya")])
    def test_update_fields_of_authorized_user(self, access_token, field, value):
        user_methods = UserMethods()
        payload = {field: value}
        access_token = access_token
        response = user_methods.update_user_data(access_token, payload)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Проверка возможности обновления данных неавторизованного пользователя.')
    @pytest.mark.parametrize('field, value', [
        ("email", "dchernukha27@mail.ru"),
        ("password", "1234567"),
        ("name", "Darya")])
    def test_update_fields_of_unauthorized_user(self, access_token, field, value):
        user_methods = UserMethods()
        payload = {field: value}
        response = user_methods.update_user_data('', payload)
        assert response.status_code == 401 and response.json() == error_of_authorization_response
