from django.contrib import admin
from apppedido.models import Avatar, Cliente, Producto, Pedido, Repartidor

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Repartidor)
admin.site.register(Avatar)
