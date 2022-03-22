from django.db import models

# Create your models here.

class Cliente(models.Model):
    num_celular = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    localidad = models.CharField(max_length=40)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()  

class Repartidor(models.Model):
    id_repartidor = models.CharField(max_length=4 ,primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    num_celular = models.CharField(max_length=40)
    sexos = [
        ("F", "Femenino"), 
        ("M", "Masculino"), 
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default="F")
    

    def nombreCompleto(self):
        txt = "{0} {1}"
        return txt.format(self.apellido, self.nombre)

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    repartidor = models.ForeignKey(Repartidor, null=True, blank=True, on_delete=models.CASCADE)


