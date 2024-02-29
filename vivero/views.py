from django.shortcuts import render
from .models import *

def vivero(request):
	frase_inicio=FraseInicio.objects.all()
	productos=Producto.objects.all()
	columnas_quienes=QuienesSomos.objects.all()
	imagenes_carrusel=Carrusel.objects.all()
	context = {'frase_inicio': frase_inicio, 'productos': productos, 'columnas_quienes': columnas_quienes, 'imagenes_carrusel': imagenes_carrusel}
	return render(request, 'vivero/vivero.html', context)
