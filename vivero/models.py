from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
# Create your models here.

class Color(models.Model):
    color_fondos = ColorField(verbose_name="Color de los fondos", default="#B2BD7E")
    hover_header = ColorField(verbose_name="Color de activación de botones en Header", default="#749C75")
    hover_carrusel = ColorField(verbose_name="Color de activación de botones en Carrusel", default="#749C75")
    hover_productos = ColorField(verbose_name="Color de activación de cuadro de cada producto", default="#5D4A66")
    hover_redes = ColorField(verbose_name="Color de activación de redes del footer", default="#E9D985")
    header_texto_botones = ColorField(verbose_name="Color de texto de botones en header", default="#fff")
    fondo_header = ColorField(verbose_name="Color de fondo del header", default="#5D4A66")
    fondo_secciones = ColorField(verbose_name="Color de los fondos de cada título de sección", default="#6A5D7B")
    frase_principal = ColorField(verbose_name="Color de texto de la frase principal", default="#6A5D7B")
    carrusel_fondo_texto = ColorField(verbose_name="Color de fondo del texto dentro del Carrusel", default="#749C75")
    carrusel_texto = ColorField(verbose_name="Color de texto dentro del Carrusel", default="#ffffff")
    titulos_secciones = ColorField(verbose_name="Color de cada título de sección", default="whitesmoke")
    productos_quienes_form_texto_detalles = ColorField(verbose_name="Color de texto de los productos, sección quienes y formulario", default="#6A5D7B")
    productos_fondo = ColorField(verbose_name="Color de fondo de los cuadros de productos", default="whitesmoke")
    form_boton = ColorField(verbose_name="Color de fondo del botón de formulario", default="#6A5D7B")
    form_texto_boton = ColorField(verbose_name="Color de texto del botón del formulario", default="white")
    footer_texto = ColorField(verbose_name="Color de texto del footer", default="#e9e9e9")

    def __str__(self):
        return "Configuración de colores"


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
    
class Logos(models.Model):
    logo_header=models.ImageField(null=True, blank=True)
    logo_form=models.ImageField(null=True, blank=True)
    logo_footer=models.ImageField(null=True, blank=True)
    
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