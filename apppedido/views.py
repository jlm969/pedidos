#from turtle import title
#from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from datetime import datetime
from apppedido.models import *
 #importamos la clase Form de django
from apppedido.forms import ProductoFormulario, ClienteFormulario, RepartidorFormulario



# Create your views here.

def inicio(request):
    dict_ctx = {"title": "Inicio", "page": "DELIVERY - PEDIDOS WEB"}
    return render(request, "apppedido/index.html", dict_ctx)

def pedidos(request):
    return render(request, "apppedido/pedidos.html",{"title":"Pedidos", "page":"EN CONSTRUCCION..."})

def productos(request):
    productos = Producto.objects.all()

    if request.method == 'POST':
        producto = ProductoFormulario(request.POST)
        if producto.is_valid():    
            datos = producto.cleaned_data
            producto_nuevo = Producto(datos['id_producto'], datos['nombre'], datos['precio'])        
            producto_nuevo.save()
            
            formulario = ProductoFormulario()
            return render(request, "apppedido/productos.html",{"productos":productos, "title":"Productos", "page":"Productos","formulario":formulario})
    else:

        formulario = ProductoFormulario()
        return render(request, "apppedido/productos.html",{"productos":productos, "title":"Productos", "page":"Productos","formulario":formulario})


def repartidores(request):
    repartidores = Repartidor.objects.all()

    if request.method == 'POST':
        repartidor = RepartidorFormulario(request.POST)
        if repartidor.is_valid():    
            datos = repartidor.cleaned_data

            repartidor_nuevo = Repartidor(datos['id_repartidor'], datos['nombre'], datos['apellido'], datos['direccion'], datos['email'], datos['num_celular'], datos['sexo'])        
            repartidor_nuevo.save()
            
            formulario = RepartidorFormulario()
            return render(request, "apppedido/repartidores.html",{"repartidores":repartidores, "title":"Repartidores", "page":"Repartidores","formulario":formulario})
    else:

        formulario = RepartidorFormulario()
        return render(request, "apppedido/repartidores.html",{"repartidores":repartidores, "title":"Repartidores", "page":"Repartidores","formulario":formulario})


def clientes (request):
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        cliente = ClienteFormulario(request.POST)
        if cliente.is_valid():    
            datos = cliente.cleaned_data

            cliente_nuevo = Cliente(datos['celular'], datos['nombre'], datos['apellido'], datos['direccion'], datos['email'], datos['localidad'],)        
            cliente_nuevo.save()
            
            formulario = ClienteFormulario()
            return render(request, "apppedido/clientes.html",{"clientes":clientes, "title":"Clientes", "page":"Clientes","formulario":formulario})
    else:

        formulario = ClienteFormulario()
        return render(request, "apppedido/clientes.html",{"clientes":clientes, "title":"Clientes", "page":"Clientes","formulario":formulario})


def buscar_producto(request):
    data = request.GET.get('id_producto')
    error =""
    if data:
        try:
           producto = Producto.objects.get(id_producto=data)
           mensaje="Producto encontrado:"
           return render(request, "apppedido/buscarProducto.html", {'mensaje':mensaje,'page':producto})
           #return render(request, "apppedido/buscarProducto.html", {'producto':producto}) 
           #return render(request, "apppedido/buscarProducto.html", {'producto':producto[0]}) 
        except Exception as exc:
            print(exc)
            error = "No existe el producto"
    return render(request, "apppedido/buscarProducto.html", {"page": error}) #le paso una plantilla .html
    #return render(request, "apppedido/buscarProducto.html", {"error": error}) #le paso una plantilla .html


def eliminar_producto(request, codigo_producto):
    try:
        producto = Producto.objects.get(id_producto=codigo_producto)
        producto.delete()
        productos = Producto.objects.all()
        contexto= {"productos":productos}
        return render(request, "apppedido/productos.html",contexto)
    except Exception as exc:
        return render(request, "apppedido/index.html")



def actualizar_producto(request, codigo_producto):

    producto = Producto.objects.get(id_producto=codigo_producto)
  
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST)
        if formulario.is_valid():    
            data = formulario.cleaned_data
            producto.nombre = data["nombre"]
            producto.precio = data["precio"]
            producto.save()
            productos = Producto.objects.all()
            contexto= {"productos":productos}
            return render(request,"apppedido/productos.html", contexto)  
        #else:
        #   return render(request,"apppedido/index.html")    
    else:
        formulario = ProductoFormulario(initial= {"id_producto" : producto.id_producto,
                                                   "nombre":producto.nombre, "precio":producto.precio})
        return render(request,"apppedido/actualizarProducto.html", {"formulario":formulario ,"codigo_producto":codigo_producto})



def eliminar_cliente(request, num_celular):
    try:
        cliente = Cliente.objects.get(celular=num_celular)
        cliente.delete()
        clientes = Cliente.objects.all()
        contexto= {"clientes":clientes}
        return render(request, "apppedido/clientes.html",contexto)
    except Exception as exc:
        return render(request, "apppedido/index.html")


def eliminar_repartidor(request, codigo_repartidor):
    try:
        repartidor = Repartidor.objects.get(id_repartidor=codigo_repartidor)
        repartidor.delete()
        repartidores = Repartidor.objects.all()
        contexto= {"repartidores":repartidores}
        return render(request, "apppedido/repartidores.html",contexto)
    except Exception as exc:
        return render(request, "apppedido/index.html")