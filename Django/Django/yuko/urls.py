from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import homepage


urlpatterns = [
    path('', homepage, name='homepage'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)