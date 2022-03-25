from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from datetime import datetime
from apppedido.models import *
 #importamos la clase Form de django
from apppedido.forms import ProductoFormulario 


# Create your views here.

def inicio(request):
    date_init = datetime.now()
    dict_ctx = {"title": "Inicio", "message": "Bienvenid@"}
    return render(request, "apppedido/index.html", dict_ctx)

def clientes(request):
    return render(request, "apppedido/clientes.html")

def repartidores(request):
    return render(request, "apppedido/repartidores.html")

def pedidos(request):
     return render(request, "apppedido/pedidos.html")

def productos(request):
     return render(request, "apppedido/productos.html")

#Formulario  Repartidor
def form_repartidor(request):
    if request.method == 'POST':
        repartidor = Repartidor ( request.POST['id_repartidor'],
                            request.POST['nombre'],
                            request.POST['apellido'],
                            request.POST['direccion'],
                            request.POST['email'],
                            request.POST['num_celular'],
                            request.POST['sexo'])
        repartidor.save()
        return render(request, "apppedido/repartidoresForm.html")
    return render(request, "apppedido/repartidoresForm.html")


#Formulario Clientes   -  sin usar la clase Form de Django
def form_cliente(request):
    if request.method == "POST":
        cliente = Cliente( request.POST['celular'],
                            request.POST['nombre'],
                            request.POST['apellido'],
                            request.POST['direccion'],
                            request.POST['email'],
                            request.POST['direccion'])
        cliente.save()
        return render(request, "apppedido/clientesForm.html")
    return render(request, "apppedido/clientesForm.html")
# Fin Formulario Clientes   -  sin usar la clase Form de Django    

#Formulario Producto - sin usar la clase Form de Django
#def form_producto(request):
#    if request.method == 'POST':
#        producto = Producto (request.POST['id_producto'], request.POST['nombre'], request.POST['precio'])
#        producto.save()
#        return render(request, "apppedido/productosForm.html") # el template .html es el archivo dentro de App   
#    return render(request, "apppedido/productosForm.html") # el template .html es el archivo dentro de App 
# Fin Formulario Producto   -  sin usar la clase Form de Django       
#Formulario Producto - usando clase Form de Django

def form_producto(request):
    if request.method == 'POST':
        #instanciamos la clase  y recibe el request.POST
        #lee el dicci.. y le asiga automa.. a cada campo el valor que le corresponde
        
        producto = ProductoFormulario(request.POST)
         #esta llegando un formulario entero que se guarda en producto
        #chequeamos que los datos sean validos en producto con el metodo is_valid
        if producto.is_valid():    
            #creamos una variable en este caso "datos" y con el metodo clean_data limpiamos el contenido
            #para obtener los datos que se necesitan para cargar 
            datos = producto.cleaned_data
            #instanciamos un nuevo producto con la clase , pasando los valores obtenidos en datos
            producto_nuevo = Producto(datos['id_producto'], datos['nombre'], datos['precio'])        
            producto_nuevo.save()
            #una vez cargados los datos del form , redirecciono al inicio, en este caso index.html
        return render(request, "apppedido/index.html") # el template .html es el archivo dentro de App  
    else: 
        # Sino es POST , significa que quieren la pagina como tal, entonces generamos un formulario vacio
        producto_form = ProductoFormulario()
    # le pasamos un contexto
    return render(request, "apppedido/productosForm.html", {"formulario":producto_form}) # el template .html es el archivo dentro de App 

# Fin Formulario Producto   -  usando clase Form de Django   

def buscar_producto(request):

    data = request.GET['id_producto']

    if data:
        producto = Producto.objects.filter(id_producto=data)
       
        return render(request, "apppedido/buscarProducto.html", {'producto':producto[0]}) 

    return render(request, "apppedido/buscarProducto.html") #le paso una plantilla .html

