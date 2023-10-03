from django.db import models

# Create your models here.
class Animales(models.model):

    perro = models.CharField(max_length=50)
    gato = models.CharField(max_length=50)
    gallo = models.CharField(max_length=50)
    loro = models.CharField(max_length=50)
    chancho = models.CharField(max_length=50)
    tortuga = models.CharField(max_length=50)
    

