from django.db.models.indexes import Index
from django.http.response import FileResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from Servicios.serializers import *

# Create your views here. Logica del Bakc end

class UserSeriAPI(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuario.objects.all()

class SongsSeriAPI(viewsets.ModelViewSet):
    serializer_class = SongsSerializer
    queryset = Canciones.objects.all()

class GenderSeriAPI(viewsets.ModelViewSet):
    serializer_class = GenderSerializer
    queryset = GeneroMusical.objects.all()

#def Prueba(request):
    #Info del usuario
 #   return HttpResponse("Prueba de la seccion 'Servicios'")