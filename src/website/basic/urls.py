from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from basicapp import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('basicapp.urls')),
    re_path(r'^.*\.*', basicapp.views.pages, name='templates'),



]
