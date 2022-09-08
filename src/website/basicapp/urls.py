from django.contrib import admin
from django.urls import path,include, re_path
from . import views

urlpatterns = [
	path("",views.home,name="home"),
    path("send_otp",views.send_otp,name="send otp"),
    path('templates/loanApplyPage.html',views.loanApply,name="templates"),
    path('admin/', admin.site.urls),
    re_path(r'^.*\.*', views.pages, name='templates'),

]