from django.db.models.indexes import Index
from django.http.response import FileResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. Logica del Bakc end

def Prueba(request):
    #Info del usuario
    return HttpResponse("Prueba de la seccion 'Servicios'")