from django.db import models
import uuid
from django.core.management.utils import get_random_secret_key

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
  )
  senha = models.CharField(
    max_length=50,
    null=False,
    blank=True,
    default=get_random_secret_key,
  )
  data_nascimento = models.DateField(
    null=False,
    blank=False,
  )
