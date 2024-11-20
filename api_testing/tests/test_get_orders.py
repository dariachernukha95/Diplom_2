import allure

from api_testing.data import valid_ingredients_list, error_of_authorization_response
from api_testing.methods.order_methods import OrderMethods

class TestOrderGetting:

    @allure.title('Проверка возможности получения заказов авторизованного пользователя.')
    def test_get_orders_of_authorized_user(self, access_token):
        order_methods = OrderMethods()
        access_token = access_token
        order_methods.create_order(access_token, valid_ingredients_list)
        response = order_methods.get_order(access_token)
        assert response.status_code == 200 and len(response.json()["orders"]) == 1

    @allure.title('Проверка возможности получения заказов неавторизованного пользователя.')
    def test_get_orders_of_unauthorized_user(self, access_token):
        order_methods = OrderMethods()
        access_token = access_token
        order_methods.create_order(access_token, valid_ingredients_list)
        response = order_methods.get_order("")
        assert response.status_code == 401 and response.json() == error_of_authorization_response
