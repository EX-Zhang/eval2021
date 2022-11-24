from django.shortcuts import render, redirect

from django.http import JsonResponse, HttpResponse

from .Wallet import *

import json

# Create your views here.

def index(request):

    return render(request,"Wallet.html",{})

def get_Wallets(request):

    return JsonResponse(getWallets(request.session.get("username"),request.session.get("token")),safe=False)

def new_Wallet(request):

    if request.method != "POST":

        return JsonResponse({"statue":"error"})

    result = json.loads(request.body)

    addr = create_Address(request.session.get("token"))

    add_Wallet(request.session.get("username"),result.get("wallet_name"))

    add_Address(request.session.get("username"),addr,result.get("wallet_name"))

    create_Wallet(result.get("wallet_name"),addr.get("address"),request.session.get("token"))

    return JsonResponse({"statue":"success"})

def Transaction(request):

    if request.method != "POST":

        return JsonResponse({"statue":"error"})

    result = json.loads(request.body)

    return JsonResponse(start_Transaction(get_Addresses(request.session.get("username"),result.get("input")),result.get("output"),result.get("value"),request.session.get("token")),safe=False)

def add_addr(request):

    if request.method != "POST":

        return JsonResponse({"statue":"error"})

    result = json.loads(request.body)

    username = request.session.get("username")

    token = request.session.get("token")

    addr = create_Address(token)

    wallet = result.get("wallet")

    Wallet_Add_Address(wallet,addr,token)

    add_Address(addr)

    return JsonResponse({"statue":"success"})

def delete_Wallet(request):

    if request.method != "POST":

        return JsonResponse({"statue":"error"})

    result = json.loads(request.body)

    username = request.session.get("username")

    token = request.session.get("token")

    wallet = result.get("wallet")

    del_Wallet(username,wallet,token)
