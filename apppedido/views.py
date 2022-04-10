
from dataclasses import field
from re import template
from winreg import DeleteValue
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from apppedido.models import *
 #importamos la clase Form de django
from apppedido.forms import AvatarFormulario, ProductoFormulario, ClienteFormulario, RepartidorFormulario, UsuarioRegistroForm, UsuarioEditForm


# Vistas Basadas en Clases 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView


# Autenticacion Django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout , authenticate

# Mixin y Decoradores Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




# Create your views here.

def inicio(request):

    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None
    else:
        imagen = None
    dict_ctx = {"title": "Inicio", "page": "DELIVERY - PEDIDOS WEB","imagen_url": imagen}
    return render(request, "apppedido/index.html", dict_ctx)


def pedidos(request):
    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None
    return render(request, "apppedido/pedidos.html",{"title":"Pedidos", "page":"EN CONSTRUCCION...","imagen_url": imagen})



# Decoradores Django  
# antes de la vista que quiero que solo el usuario logueado puede acceder
@login_required()
def productos(request):
    productos = Producto.objects.all()

    if request.method == 'POST':
        producto = ProductoFormulario(request.POST)
        if producto.is_valid():    
            datos = producto.cleaned_data
            producto_nuevo = Producto(datos['id_producto'], datos['nombre'], datos['precio'])        
            producto_nuevo.save()
            
            formulario = ProductoFormulario()
            # return render(request, "apppedido/productos.html",{"productos":productos, "title":"Productos", "page":"Productos","formulario":formulario})
            # Utilizando redirect, (siempre en POST) pasandole el nombre de una vista a la cual quiero ir
            # Se utiliza cuando un usuario se registra
            return redirect('Inicio')

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

    
    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None
    else:
        imagen = None



    data = request.GET.get('id_producto')
    error =""
    if data:
        try:
           producto = Producto.objects.get(id_producto=data)
           mensaje="Producto encontrado:"
           return render(request, "apppedido/buscarProducto.html", {'mensaje':mensaje,'page':producto, "imagen_url": imagen })
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
            producto.nombre = data[""]
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



# Vistas Basadas en Clases 

# ListView -- Listar contenido
# A este tipo de Vistas basadas en  Clases  le puedo pasar  LoginRequiredMixin  
# para que solo un usuario logueado pueda accederla
# y va al principio!!!  
class ProductoLista(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "apppedido/productoLista.html" 

# CreateView -- Crear un item  
class ProductoCrear(CreateView):
    model = Producto
    template_name = "apppedido/productoCrear.html" 
    #success_url = "/apppedido/producto/lista"
    fields = ['id_producto', 'nombre', 'precio']
    


# UpdateView -- Actualizar  un item
class ProductoActualizar(UpdateView):
    model = Producto
    success_url = "/apppedido/producto/lista"
    fields = ['precio']


# DetailView -- obtengo un solo item
class ProductoDetalle(DetailView):
    model = Producto
    template_name = "apppedido/productoDetalle.html" 


# DeleteView -- Borrar un item
class ProductoEliminar(DeleteView):
    model = Producto
    success_url = "/apppedido/producto/lista" 



def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            nombre_usuario = data.get("username")
            contra = data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contra)

            if usuario is not None:
                login(request, usuario)
                dict_ctx = {"title": "Inicio", "mensaje": "Bienvenido!!!", "page": usuario}
                return render (request, "apppedido/index.html", dict_ctx)
            else:
                dict_ctx = {"title": "Inicio", "page": usuario, "errors":["El usuario no existe"]}
                return render (request, "apppedido/index.html", dict_ctx)
        else:
            dict_ctx = {"title": "Inicio", "page": "Usuario Anonimo", "errors":["Revise datos enviados en el formulario"]}
            return render (request, "apppedido/index.html", dict_ctx)

    else:
        form = AuthenticationForm()
        return render (request,"apppedido/login.html", {"form": form} )

def register_request(request):
    if request.method == "POST":
       # Formulario Propio de Registro
        form = UsuarioRegistroForm(request.POST)
       
       # Formulario de Registro de Django
       # form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            form.save()
            dict_ctx = {"title": "Inicio", "page": usuario}

            #return render (request,"apppedido/index.html", dict_ctx)

            # Utilizando redirect, (siempre en POST) pasandole el nombre de una vista a la cual quiero ir
            # el redirect no puede recibir un diccionario !! OJO !!
            return redirect ("Inicio")
        else:
            dict_ctx = {"title": "Inicio", "page": "Usuario Anonimo", "errors":["No paso las validaciones"]}
            return render (request, "apppedido/index.html", dict_ctx) 
            
    else:
        # Formulario Propio de Registro
        form = UsuarioRegistroForm()
        
        # Formulario de Registro de Django
        # form = UserCreationForm()

        return render (request,"apppedido/register.html", {"form": form} )

@login_required()
def actualizar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        form = UsuarioEditForm(request.POST)  #contiene los valores que vienen d ela peticion
        if form.is_valid():
            data = form.cleaned_data
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.save()
            return redirect ("Inicio")
        else:
            form = UsuarioEditForm(initial={'email':usuario.email , 'first_name':usuario.first_name,'last_name':usuario.last_name})
            #erros = {"errors":["No paso las validaciones"]}
            #return render(request, "apppedido/editar_usuario.html", {"form":form}, erros )
            form = UsuarioEditForm(initial={"email": usuario.email})  
            return render(request,  "appcoder/editar_usuario.html", {"form": form, "errors": ["Datos invalidos"]})

    else:
        form = UsuarioEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name,'last_name':usuario.last_name})
        return render(request, "apppedido/editar_usuario.html", {"form":form})

@login_required()
def cargar_imagen(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST,request.FILES)

        if formulario.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
            
        return redirect("Inicio")
    else:

        formulario = AvatarFormulario()
        return render(request, "apppedido/cargarImagen.html", {"form": formulario})