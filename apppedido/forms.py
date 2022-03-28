from django import forms

class ProductoFormulario(forms.Form):
    # Campos del Formulario
    id_producto = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    precio = forms.FloatField()

class ClienteFormulario(forms.Form):
    # Campos del Formulario
    celular = forms.CharField(max_length=15)
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    email = forms.EmailField()
    localidad = forms.CharField(max_length=40)

class RepartidorFormulario(forms.Form):
    id_repartidor = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    email = forms.EmailField()
    num_celular = forms.CharField(max_length=40)
    sexo = forms.CharField(max_length=1)
    