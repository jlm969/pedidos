from django.urls import path
from apppedido.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('clientes/', clientes, name='Clientes'),    
    path('repartidores/', repartidores, name='Repartidores'),    
    path('productos/', productos, name='Productos'),    
    path('pedidos/', pedidos, name='Pedidos'),
    path('buscarProducto/', buscar_producto, name='BuscarProducto'),
    path('eliminarProducto/<codigo_producto>/', eliminar_producto, name='EliminarProducto'),
    path('eliminarCliente/<num_celular>/', eliminar_cliente, name='EliminarCliente'),
    path('eliminarRepartidor/<codigo_repartidor>/', eliminar_repartidor, name='EliminarRepartidor'),
    path('actualizarProducto/<codigo_producto>/', actualizar_producto, name='ActualizarProducto'),
]