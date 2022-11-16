
from .models import *

import blockcypher

def login_check(username, password):

    result = User.objects.filter(username=username,password=password)

    if len(result) == 1:

        return result[0]

    return None

def signup_user(user):

    if len(User.objects.filter(username=user["username"])) != 0:

        return {"error": "Username Existed"}

    if valid_Token(user["token"]):

        return {"error": "Unvalid Token"}

    new_user = User(username=user["username"],password=user["password"],firstname=user["firstname"],lastname=user["lastname"],email=user["email"],token=user["token"])

    new_user.save()

    return {"success": "valid"}

def valid_Token(api_key):

    if 'error' in blockcypher.get_token_info(api_key):

        return False

    return True
