from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from apppedido.models import *


# Create your views here.

def inicio(request):
    date_init = datetime.now()
    dict_ctx = {"title": "Inicio", "message": "Bienvenid@"}
    return render(request, "apppedido/index.html", dict_ctx)

def clientes(request):
    return render(request, "apppedido/clientes.html")

def repartidores(request):
    return render(request, "apppedido/repartidores.html")

def pedidos(request):
     return render(request, "apppedido/pedidos.html")

def productos(request):
     return render(request, "apppedido/productos.html")