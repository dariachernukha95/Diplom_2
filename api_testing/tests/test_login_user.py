import allure

from api_testing.data import user_login_with_incorrect_email_or_password_response
from api_testing.methods.user_methods import UserMethods

class TestUserLogin():

    @allure.title('Проверка успешного логина пользователя.')
    def test_success_user_login(self, email_password):
        user_methods = UserMethods()
        payload = email_password
        response = user_methods.login_user(payload)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Проверка возможности логина пользователя с некорректным email.')
    def test_login_user_with_incorrect_email(self, email_password):
        user_methods = UserMethods()
        payload = {"email": "dariachernukha95",
                   "password": email_password["password"]
                   }
        response = user_methods.login_user(payload)
        assert response.status_code == 401 and response.json() == user_login_with_incorrect_email_or_password_response

    @allure.title('Проверка возможности логина пользователя с некорректным паролем.')
    def test_login_user_with_incorrect_password(self, email_password):
        user_methods = UserMethods()
        payload = {"email": email_password["email"],
                   "password": "123"
                   }
        response = user_methods.login_user(payload)
        assert response.status_code == 401 and response.json() == user_login_with_incorrect_email_or_password_response
