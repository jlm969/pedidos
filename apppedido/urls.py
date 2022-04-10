from django.urls import path
from apppedido.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('login/', login_request, name='login'),
    path('register/', register_request, name='Register'),
    path('logout/', LogoutView.as_view(template_name="apppedido/logout.html"), name='logout'),
    path('editar/', actualizar_usuario, name='edit'),

    path('clientes/', clientes, name='Clientes'),    
    path('repartidores/', repartidores, name='Repartidores'),    
    path('productos/', productos, name='Productos'),    
    path('pedidos/', pedidos, name='Pedidos'),
    path('buscarProducto/', buscar_producto, name='BuscarProducto'),
    path('eliminarProducto/<codigo_producto>/', eliminar_producto, name='EliminarProducto'),
    path('eliminarCliente/<num_celular>/', eliminar_cliente, name='EliminarCliente'),
    path('eliminarRepartidor/<codigo_repartidor>/', eliminar_repartidor, name='EliminarRepartidor'),
    path('actualizarProducto/<codigo_producto>/', actualizar_producto, name='ActualizarProducto'),
 
  # A la url
    path('producto/lista/', ProductoLista.as_view(), name="productoLista"),
    path('producto/nuevo/', ProductoCrear.as_view(), name="productoCrear"),
    path('producto/detalle/<pk>/', ProductoDetalle.as_view(), name="productoDetalle"),
    path('producto/editar/<pk>/', ProductoActualizar.as_view(), name="productoActualizar"),
    path('producto/eliminar/<pk>/', ProductoEliminar.as_view(), name="productoEliminar"),

    path("cargar_imagen/", cargar_imagen, name="CargarImagen")
]