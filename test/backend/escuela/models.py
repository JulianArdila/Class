from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.


class Escuela(models.Model):
    nombre = models.CharField(max_length=200)
    address = map_fields.AddressField(max_length=200, verbose_name='Dirección',
                                      blank=True, null=True)
    geolocation = map_fields.GeoLocationField(max_length=100,
                                          verbose_name='Coordenadas', blank=True, null=True)

