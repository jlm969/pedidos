from django.urls import path
from apppedido.views import inicio, clientes, repartidores, productos, pedidos

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('clientes/', clientes, name='Clientes'),    
    path('repartidores/', repartidores, name='Repartidores'),    
    path('productos/', productos, name='Productos'),    
    path('pedidos/', pedidos, name='Pedidos'),
]