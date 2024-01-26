from django.shortcuts import render
from .models import *

def vivero(request):
	productos=Producto.objects.all()
	context = {'productos':productos}
	return render(request, 'vivero/vivero.html', context)

'''def cart(request):
	context = {}
	return render(request, 'vivero/cart.html', context)'''
