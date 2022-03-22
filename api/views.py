from api.serializers import UsuariosSerializer
from rest_framework import viewsets, permissions
from api.models import Usuarios
from django.shortcuts import render

class UsuariosViewSet(viewsets.ModelViewSet):
  queryset = Usuarios.objects.all()
  serializer_class = UsuariosSerializer
  permission_class = [permissions.IsAuthenticated]
