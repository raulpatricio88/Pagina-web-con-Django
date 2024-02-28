from django.shortcuts import render, redirect
from .models import Categoria, Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ProductoForm

# Create your views here.
def inicio(request):
    return render(request, 'Index.html')

def contactanos(request):
    return render (request, 'Contactanos.html')

def galeria(request):
    return render (request, 'Galeria.html')

def nosotros(request):
    return render (request, 'Nosotros.html')

@login_required
def crud(request):
    productos = Producto.objects.all()  #similar a select * from Vehiculo
    datos={
        'productos':productos
    }
    return render(request, 'crud.html', datos)    

@login_required
def crearProducto(request):
    if request.method=='POST':
        #creamos un objeto de tipo ProductoForm
        producto_form = ProductoForm(request.POST, request.FILES)   
        if producto_form.is_valid():  #controla que el objeto tenga toda la informacion de los atributos (que este integramente creado)
            #almacena el objeto en el backend
            producto_form.save() #similar al insert de una BDR
            return redirect('crud') 
    else:
        producto_form= ProductoForm()
    return render(request, 'crearProducto.html', {'producto_form': producto_form})  

@login_required
def eliminar(request, id):
    producto = Producto.objects.get(idProducto=id) #similar a select * from where patente = id
    producto.delete() #eliminacion fisica del backend
    return redirect ('crud')

@login_required
def modificar(request, id):
    producto = Producto.objects.get(idProducto=id)    
    datos ={
        'formMod' : ProductoForm(instance=producto) #instanciamos un objeto encontrado en un formulario de tipo producto
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()    #se utiliza para crear y modificar
            return redirect('crud')
    return render(request, 'modificar.html', datos)   

def carrito(request):
    productos = Producto.objects.all()  #similar a select * from Vehiculo
    datos={
        'productos':productos
    }
    return render(request, 'carrito.html', datos)          