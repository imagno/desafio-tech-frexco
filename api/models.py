from django.db import models
from random import choice
import uuid
import string

senha = ''
tamanho_senha = 10
caracteres = string.ascii_letters + string.digits + string.punctuation
  
def gerar_senha(senha, tamanho_senha, caracteres):
  for i in range(tamanho_senha):
    senha += choice(caracteres)
    
  return senha
  
default_key = gerar_senha(senha, tamanho_senha, caracteres)

class Usuarios(models.Model):
  
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    null=False,
    blank=True,
  )
  login = models.CharField(
    max_length=8,
    null=False,
    blank=False,
    unique=True,
  )
  senha = models.CharField(
    max_length=15,
    default=default_key,
    null=False,
    blank=True,
  )
  data_nascimento = models.DateField(
    null=False,
    blank=False,
  )
