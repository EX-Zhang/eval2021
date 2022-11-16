from django.shortcuts import render, redirect

from django.http import JsonResponse, HttpResponse

from .Wallet import *

# Create your views here.

def index(request):

    return render(request,"Wallet.html",{})

def get_Wallets(request):

    return JsonResponse(getWallets(request.session.get("username"),request.session.get("token")),safe=False)

def new_Wallet(request):

    if request.method != "POST":

        return JsonResponse()

    result = json.loads(request.body)

    addr = create_Address(request.session.get("token"))

    create_Wallet(result.get("wallet_name"),addr,request.session.get("token"))

def Transaction(request):

    if request.method != "POST":

        return JsonResponse()

    result = json.loads(request.body)

    return JsonResponse(start_Transaction(get_Addresses(request.session.get("username"),result.get("input")),result.get("output"),result.get("value"),request.session.get("token")),safe=False)

def add_addr(request):

    if request.method != "POST":

        return JsonResponse()

    result = json.loads(request.body)

    username = request.session.get("username")

    token = request.session.get("token")

    addr = create_Address(token)

    wallet = result.get("wallet")

    Wallet_Add_Address(wallet,addr,token)

    add_Address(addr)

    
