import allure
import pytest

from api_testing.data import existed_user_creation_response,user_creation_without_one_of_fields_response
from api_testing.methods.user_methods import UserMethods
from api_testing.helpers import generate_full_data_for_user_creation

class TestUserCreation():

    @allure.title('Проверка возможности создания пользователя.')
    def test_success_user_creation(self):
        user_methods = UserMethods()
        payload = generate_full_data_for_user_creation()
        response = user_methods.create_user(payload)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Проверка возможности создания пользователя, который уже зарегистрирован.')
    def test_creation_of_existed_user(self):
        user_methods = UserMethods()
        payload = generate_full_data_for_user_creation()
        user_methods.create_user(payload)
        response = user_methods.create_user(payload)
        assert response.status_code == 403 and response.json() == existed_user_creation_response

    @allure.title('Проверка возможности создания пользователя при незаполнении одного из обязательных полей.')
    @pytest.mark.parametrize('field',
                             ["email", "password", "name"])
    def test_user_creation_without_one_of_fields(self, field):
        user_methods = UserMethods()
        payload = generate_full_data_for_user_creation()
        del payload[field]
        response = user_methods.create_user(payload)
        assert response.status_code == 403 and response.json() == user_creation_without_one_of_fields_response


