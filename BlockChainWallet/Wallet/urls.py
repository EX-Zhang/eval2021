
from django.urls import path

from . import views

urlpatterns = [

    path("getWallets/",views.get_Wallets),

    path("createWallet/",views.new_Wallet),

    path("startTransaction/",views.Transaction),

    path("addAddr/",views.add_addr),

    path("deleteWallet/",views.delete_Wallet),

    path("",views.index),

]
