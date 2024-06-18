from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('form/', views.FormPage.as_view(), name='form'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
