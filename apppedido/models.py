from re import A
from django.db import models

# Create your models here.

class Cliente(models.Model):
    celular = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    localidad = models.CharField(max_length=40)
    
    def __str__(self):
        txt = "{0} {1}  - {2}"
        return txt.format(self.nombre , self.apellido, self.direccion)
           

class Producto(models.Model):
    id_producto = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()  

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

class Repartidor(models.Model):
    id_repartidor = models.PositiveSmallIntegerField(primary_key=True)
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
    

    def __str__(self):
        txt = "{0} -  {1} {2}"
        return txt.format(self.id_repartidor, self.nombre , self.apellido)

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    repartidor = models.ForeignKey(Repartidor, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        txt = "Nro. Pedido: {0} Cliente: {1} Productos:  {2}    Repartidor: {3}     Fecha: {4}"
        if self.repartidor==None:
            reparto="RETIRA EN LOCAL"        
        else:
            reparto=self.repartidor

        fechaPedido = self.fecha.strftime("%d/%m/%Y %H:%M:%S")    
        return txt.format(self.id_pedido,  self.cliente, self.producto, reparto, fechaPedido)
       # return txt.format(self.id_pedido, self.producto, self.cliente, self.repartidor, self.fecha)
