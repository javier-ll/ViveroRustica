from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''class FraseInicio(models.Model):
    '''

class QuienesSomos(models.Model):
    titulo_columna=models.CharField(max_length=100)
    texto_columna=models.CharField(default='Texto de columna de sección Quiénes somos', max_length=500)
    imagen_columna=models.ImageField(null=True, blank=True)

    @property
    def imagenURL(self):
        try:
            url=self.imagen_columna.url
        except:
            url=''
        return url

class Carrusel(models.Model):
    imagen_carrusel=models.ImageField(null=True, blank=True)
    frase_carrusel=models.CharField(default='Frase de imagen del carrusel', max_length=100)

    @property
    def imagenURL(self):
        try:
            url=self.imagen_carrusel.url
        except:
            url=''
        return url
    
class Producto(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(default='Descripción del producto', max_length=500)
    precio=models.FloatField()
    imagen=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    @property
    def imagenURL(self):
        try:
            url=self.imagen.url
        except:
            url=''
        return url