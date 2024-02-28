#creamos una o mas clases para enlazarlas con clases creadas en models.py y 
#con los templates que necesitaremos implementar (create, modify)

from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField #para enlazar el atributo categoria (es un select, es para que lo muestre como combo)
from .models import Categoria, Producto
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

#clase aplicada a la creación de usuarios
class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

#crearemos una plantilla (clase) de tipo form para Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto #con que clase vamos a (enlazar) comenzar el formulario
        fields = ['idProducto', 'nombreProducto', 'descripcionProducto', 'imagen', 'categoriaProducto', 'precioProducto', 'stockProducto'] #llamamos a los atributos de Vehiculo
        labels ={ #diccionario
            'idProducto': 'ID', #a la izq es atributo a la derecha el texto que va a ver
            'nombreProducto' : 'Nombre',
            'descripcionProducto' : 'Descripcion',
            'imagen' : 'Imagen',
            'categoriaProducto' : 'Categoria',
            'precioProducto' : 'Precio',
            'stockProducto' : 'Stock',
            

        }
        #un widget es un atajo
        widgets={
            'idProducto': forms.NumberInput(
                attrs={ #attrs significa atributos
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID de producto',
                    'id': 'idProducto'
                }
            ),
            'nombreProducto' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre de producto',
                    'id': 'nombreProducto'
                }

            ),
            'descripcionProducto' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripcion del producto',
                    'id': 'descripcionProducto'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            'categoriaProducto': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoriaProducto'
                }

            ),
            'precioProducto' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio del producto',
                    'id': 'precioProducto'
                }
            ),
            'stockProducto' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese stock del producto',
                    'id': 'stockProducto'
                }
            )

        } 

 #se puede añadir otras clases de tipo form