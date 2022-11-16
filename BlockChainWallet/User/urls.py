
from django.urls import path

from . import views

urlpatterns = [

    path("",views.Index),

    path("login/",views.login),

    path("signup/",views.signup),

]
