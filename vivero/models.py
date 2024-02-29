from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FraseInicio(models.Model):
    frase = models.CharField(default='Frase principal', max_length=50)
    imagen_inicio = models.ImageField(upload_to='frase_inicio/', null=True, blank=True)

    # Sobrescribir el método save para permitir solo un objeto FraseInicio en la base de datos
    def save(self, *args, **kwargs):
        # Verificar si ya existe un objeto FraseInicio en la base de datos
        if FraseInicio.objects.exists() and not self.pk:
            # Si existe, obtener el objeto y actualizar sus atributos con los del nuevo objeto
            existente = FraseInicio.objects.first()
            existente.frase = self.frase
            existente.imagen_inicio = self.imagen_inicio
            existente.save()
            # Retornar el objeto existente sin guardar el nuevo objeto
            return existente
        # Si no existe ningún objeto FraseInicio, guardar el objeto normalmente
        return super().save(*args, **kwargs)

    @property
    def imagenURL(self):
        try:
            url = self.imagen_inicio.url
        except:
            url = ''
        return url


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