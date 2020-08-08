from django import forms
from aplicacion.models import *


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion',
                  'precio',
                  'stock',
                  'iva')
        label = {
            'descripcion': 'Producto',
            'precio': 'Precio',
            'stock': 'Stock',
            'iva':'Iva'}
        widgets={

            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre del producto'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'type':'number',
                    'step':'any',
                    'value':'0',
                    'class': 'form-control'

                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control'

                }
            ),
            'iva': forms.CheckboxInput(
                attrs={
                    'class': 'field-iva'

                }
            )
        }



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc',
                  'nombre',
                  'direccion',
                  'producto')
        label = {
            'ruc': 'Ruc',
            'nombre': 'Nombre del Cliente',
            'direccion': 'Dirección'}
        widgets={

            'ruc':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Ruc'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre del cliente'

                }
            ),
            'direccion': forms.Textarea(
                attrs={
                    'class': 'form-control'

                }
            ),
            'producto': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }