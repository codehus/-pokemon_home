from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    generacion = models.CharField(max_length=20,default='Sin generacion')