from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path("",views.home,name="home"),
    path("send_otp",views.send_otp,name="send otp")]