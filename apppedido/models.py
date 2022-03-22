from django.db import models

# Create your models here.

class Cliente(models.Model):
    num_celular = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    localidad = models.CharField(max_length=40)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()    

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)


class Repartidor(models.Model):
    id_repartdir = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    num_celular = models.IntegerField()
    sexos = [
        ("F", "Femenino"), 
        ("M", "Masculino"), 
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default="F")
    pedido = models.ForeignKey(Pedido, null=False, blank=False, on_delete=models.CASCADE)

    def nombreCompleto(self):
        return (self.apellido, self.nombre)
