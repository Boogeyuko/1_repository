
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('leaf/', admin.site.urls),
    path('', include('yuko.urls')),
]
