from django.shortcuts import render
from .models import *

def vivero(request):
	frase_inicio=FraseInicio.objects.first()
	# Si no hay ninguna instancia de FraseInicio, crear una con valores predeterminados
	if not frase_inicio:
		frase_inicio = FraseInicio.objects.create(frase='Frase principal predeterminada')
	colores=Color.objects.first()   
	productos=Producto.objects.all()
	columnas_quienes=QuienesSomos.objects.all()
	imagenes_carrusel=Carrusel.objects.all()
	logos=Logos.objects.all()
	context = {'frase_inicio': frase_inicio, 'productos': productos,
			'columnas_quienes': columnas_quienes,
			'imagenes_carrusel': imagenes_carrusel,
			'logos': logos,
			'colores':colores}
	return render(request, 'vivero/vivero.html', context)
