from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place/<int:id>', views.endpoint, name='endpoint')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)