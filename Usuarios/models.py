from django.db import models
from django.contrib.auth.models import AbstractUser
from aperturaAdultos.models import SERVICIOS_CHOICES
from django.urls import reverse

# Create your models here.

class CustomUser(AbstractUser):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    servicio = models.CharField(max_length=100, choices = SERVICIOS_CHOICES)

    def __str__(self):

        return self.nombre


