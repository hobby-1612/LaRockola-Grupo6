from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Servicios.views import *

router = DefaultRouter()
router.register('usuarios', UserSeriAPI)
router.register('listacanciones', SongsSeriAPI)
router.register('generos', GenderSeriAPI)
router.register('perfiles', ProfileAPI)


urlpatterns = [
    #path('ejemplo', Prueba)
    path('crud/', include(router.urls))
]