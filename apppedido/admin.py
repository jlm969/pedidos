from django.contrib import admin
from apppedido.models import Cliente, Producto, Pedido, Repartidor

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Repartidor)
