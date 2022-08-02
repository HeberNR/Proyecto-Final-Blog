from django.urls import path
from django.views import View
from . import views


urlpatterns = [
    path('registro/', views.Registro.as_view(), name='registro'),
    
    
]