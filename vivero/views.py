from django.shortcuts import render
from .models import *

def vivero(request):
	productos=Producto.objects.all()
	columnas_quienes=QuienesSomos.objects.all()
	imagenes_carrusel=Carrusel.objects.all()
	context = {'productos': productos, 'columnas_quienes': columnas_quienes, 'imagenes_carrusel': imagenes_carrusel}
	return render(request, 'vivero/vivero.html', context)
