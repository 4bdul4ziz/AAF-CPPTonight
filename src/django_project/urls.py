from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path('finsure/', include('finsure.urls')),
    path('admin/', admin.site.urls)
]
