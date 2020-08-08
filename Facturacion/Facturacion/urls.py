"""Facturacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from aplicacion.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',menu,name='index'),#PAGINA PRINCIPAL
    path('nuevoProducto/',producto, name='producto'),#MENU PRODUCTO
    path('editarProducto/<int:id>/',editarProducto, name='editarProducto'),#MENU PRODUCTO
    path('producto/',listarProducto, name='listarProducto'),#MENU PRODUCTO
    path('eliminarProducto/<int:id>/',eliminarProducto,name='eliminarProducto'),#MENU PRODUCTO



    path('venta/',listarVenta, name='venta'),#MENU VENTAS




    path('nuevoCliente/', cliente, name='cliente'),  # MENU CLIENTE
    path('editarCliente/<int:id>/', editarCliente, name='editarCliente'),    # MENU CLIENTE
    path('cliente/', listarCliente, name='listarCliente'),    # MENU CLIENTE
    path('eliminarCliente/<int:id>/', eliminarCliente, name='eliminarCliente'),  # MENU CLIENTE
]
