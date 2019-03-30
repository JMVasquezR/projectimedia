from django.db import models


class RegistroModel(models.Model):
    cantidad_de_usuario = models.IntegerField(null=False, blank=False)
    correo_emisor = models.CharField(null=False, blank=False, max_length=100)
    asunto = models.CharField(null=False, blank=False, max_length=100)
    mensaje = models.CharField(null=False, blank=False, max_length=500)
