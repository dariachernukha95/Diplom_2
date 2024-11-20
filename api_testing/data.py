base_url = 'https://stellarburgers.nomoreparties.site/'
create_user_endpoint = 'api/auth/register'
login_user_endpoint = 'api/auth/login'
delete_user_endpoint = 'api/auth/user'
update_user_endpoint = 'api/auth/user'
order_endpoint = 'api/orders'

existed_user_creation_response = {
    "success": False,
    "message": "User already exists"
}

user_creation_without_one_of_fields_response = {
    "success": False,
    "message": "Email, password and name are required fields"
}

user_login_with_incorrect_email_or_password_response = {
    "success": False,
    "message": "email or password are incorrect"
}

error_of_authorization_response = {
    "success": False,
    "message": "You should be authorised"
}

error_of_creation_without_ingredients_response = {
    "success": False,
    "message": "Ingredient ids must be provided"
}

valid_ingredients_list = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f",
                          "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa79"]

invalid_ingredients_list = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "123"]
