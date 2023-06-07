from django.contrib import admin
from django.urls import path, include
from .views import mainpage, about
from .views import yuko

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('about/', about, name='about'),
    path('yuko/', yuko, name='yuko'),
]
