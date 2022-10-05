from unittest.util import _MAX_LENGTH
from django.db import models

class Familiar (models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    nacionalidad = models.CharField(max_length = 50)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null = True)