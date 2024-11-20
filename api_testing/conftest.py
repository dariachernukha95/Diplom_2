import pytest
from api_testing.helpers import create_new_user_and_return_user_data
from api_testing.methods.user_methods import UserMethods

@pytest.fixture
def email_password():
    email_password, access_token = create_new_user_and_return_user_data()
    yield email_password
    user_methods = UserMethods()
    user_methods.delete_user(access_token)

@pytest.fixture
def access_token():
    email_password, access_token = create_new_user_and_return_user_data()
    yield access_token
    user_methods = UserMethods()
    user_methods.delete_user(access_token)
