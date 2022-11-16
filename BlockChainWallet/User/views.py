from django.shortcuts import render, redirect

from django.http import JsonResponse

from .User import *

import json

# Create your views here.

def Index(request):

    if "username" in request.session:

        return redirect("/wallet")

    return render(request,"index.html",{})

def login(request):

    if request.method != "POST":

        return JsonResponse()

    result = json.loads(request.body)

    user = login_check(result.get("username"),result.get("password"))

    if user == None:

        return JsonResponse({"error": "Invalid Username or Password"})

    request.session["username"] = user.username

    request.session["firstname"] = user.firstname

    request.session["token"] = user.token

    return JsonResponse({"Result": "Success"})

def signup(request):

    if request.method != "POST":

        return JsonResponse()

    result = json.loads(request.body)

    user = {

        "username": result.get("username"),

        "password": result.get("password"),

        "firstname": result.get("firstname"),

        "lastname": result.get("lastname"),

        "email": result.get("email"),

        "token": result.get("token"),
        
    }

    return JsonResponse(signup_user(user))
    
