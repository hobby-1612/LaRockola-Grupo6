from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from Servicios.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = Usuario
        fields = "__all__"

class GenderSerializer(serializers.ModelSerializer):
    class Meta():
        model = GeneroMusical
        fields = "__all__"

class SongsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Canciones
        fields = "__all__"






