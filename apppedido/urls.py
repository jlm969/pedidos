from django.urls import path
from apppedido.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('clientes/', clientes, name='Clientes'),    
    path('repartidores/', repartidores, name='Repartidores'),    
    path('productos/', productos, name='Productos'),    
    path('pedidos/', pedidos, name='Pedidos'),
    path('buscarProducto/', buscar_producto, name='BuscarProducto'),
]