from django import forms

class ProductoFormulario(forms.Form):
    # Campos del Formulario
    id_producto = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    precio = forms.FloatField()
