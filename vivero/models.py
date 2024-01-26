from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''class Cliente(models.Model):
    usuario=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre'''
    
class Producto(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(default='Descripción del producto', max_length=500)
    precio=models.FloatField()
    digital=models.BooleanField(default=False, null=True, blank=True)
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