from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
from aplicacion.forms import *


def menu(request):
    opciones = {'menu': 'Menú Principal','venta': 'Venta', 'producto': 'Producto',
                'cliente': 'Cliente', 'administrar': 'Administrador'}

    return render(request, 'principal.html', opciones)


def venta(request):
    opciones = {'menu': 'Menú Principal','venta': 'Venta', 'producto': 'Producto',
                'cliente': 'Cliente', 'administrar': 'Administrador'}
    if request.method == 'POST':
        pass

    else:
        pass
    return render(request, 'venta.html', opciones)



def producto(request):
    opciones = {'menu': 'Menú Principal','venta': 'Venta', 'producto': 'Producto',
                'cliente': 'Cliente', 'administrar': 'Administrador', 'accion':'crear'}
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarProducto')
    else:
        form = ProductoForm()
        opciones['form'] = form

    return render(request, 'producto.html', opciones)

def editarProducto(request, id):
    opciones = {'menu': 'Menú Principal','venta': 'Venta', 'producto': 'Producto',
                'cliente': 'Cliente', 'administrar': 'Administrador', 'accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarProducto')

    return render(request, 'producto.html', opciones)

def listarProducto(request):
    producto = Producto.objects.all()
    opciones = {'menu': 'Menú Principal', 'venta': 'Venta', 'producto': 'Producto',
                'cliente': 'Cliente', 'administrar': 'Administrador', 'productos': producto}
    return render(request, 'listar_producto.html', opciones)

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarProducto')
    return render(request, 'eliminar_producto.html', {'producto': producto})








def cliente(request):
    opciones = {'menu': 'Menú Principal','venta': 'Venta', 'producto': 'Producto',
                'cliente': 'Cliente', 'administrar': 'Administrador', 'accion':'crear'}
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarCliente')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, 'cliente.html', opciones)

def editarCliente(request, id):
    opciones = {'menu': 'Menú Principal','venta': 'Venta', 'producto': 'Producto',
                'cliente': 'Cliente', 'administrar': 'Administrador', 'accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarCliente')

    return render(request, 'cliente.html', opciones)

def listarCliente(request):
    cliente = Cliente.objects.all()
    opciones = {'menu': 'Menú Principal', 'venta': 'Venta', 'producto': 'Producto',
                'cliente': 'Cliente', 'administrar': 'Administrador', 'clientes': cliente}
    return render(request, 'listar_cliente.html', opciones)

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarCliente')
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})



def listarVenta(request):
    factura = Factura.objects.all()
    opciones = {'menu': 'Menú Principal', 'venta': 'Venta', 'producto': 'Producto',
                'cliente': 'Cliente', 'administrar': 'Administrador', 'facturas': factura}
    return render(request, 'venta.html', opciones)