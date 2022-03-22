from dataclasses import fields
from rest_framework import serializers
from api.models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuarios
    fields = [
      'id',
      'login',
      'senha',
      'data_nascimento'
    ]