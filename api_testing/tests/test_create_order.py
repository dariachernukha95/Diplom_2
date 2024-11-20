import allure

from api_testing.methods.order_methods import OrderMethods
from api_testing.data import valid_ingredients_list, invalid_ingredients_list, error_of_creation_without_ingredients_response

class TestOrderCreation:

    @allure.title('Проверка возможности создания заказа авторизованным пользователем.')
    def test_create_order_by_authorized__user(self, access_token):
        order_methods = OrderMethods()
        access_token = access_token
        ingredients_list = valid_ingredients_list
        response = order_methods.create_order(access_token, ingredients_list)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Проверка возможности создания заказа неавторизованным пользователем.')
    def test_create_order_by_unauthorized_user(self):
        order_methods = OrderMethods()
        ingredients_list = valid_ingredients_list
        response = order_methods.create_order("", ingredients_list)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Проверка возможности создания заказа с неверным хешем ингредиентов.')
    def test_create_order_with_invalid_ingredients(self, access_token):
        order_methods = OrderMethods()
        access_token = access_token
        ingredients_list = invalid_ingredients_list
        response = order_methods.create_order(access_token, ingredients_list)
        assert response.status_code == 500

    @allure.title('Проверка возможности создания заказа без ингредиентов.')
    def test_create_order_without_ingredients(self, access_token):
        order_methods = OrderMethods()
        access_token = access_token
        ingredients_list = []
        response = order_methods.create_order(access_token, ingredients_list)
        assert response.status_code == 400 and response.json() == error_of_creation_without_ingredients_response
