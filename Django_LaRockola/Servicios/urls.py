from django.urls import path
from Servicios.views import Prueba

urlpatterns = [
    path('ejemplo', Prueba)
]