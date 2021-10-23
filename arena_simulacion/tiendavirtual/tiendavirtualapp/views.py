from builtins import range
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context,loader
from tiendavirtualapp.models import Categorias,Clientes,Productos,ProductosPedido,Inventario,Calificacion
# Create your views here.

def home(request):
    # Obtener inicialmente las categorias
    all_cat = Categorias.objects.all().order_by('id')
    # si pongo un signo menos lo ordena de forma descendente
    latest_prod = Productos.objects.all().order_by('-id')[:6]
    # Ordenar los productos por calificacion 
    top_prod = Calificacion.objects.all().order_by('-calificacion')[:6]
    latest_review = Calificacion.objects.all().order_by('-id')[:6]
    return render(request,"home.html",{"all_cat":all_cat,"latest_prod":latest_prod,"top_prod":top_prod,"latest_review":latest_review})

def lista_productos(request):
    return render(request,"shop-grid.html")

def producto_detalles(request,product_id):
    producto = get_object_or_404(Productos,pk = product_id)
    productos_relacionados = Productos.objects.filter(categoria_id = producto.categoria.id)
    calificaciones = Calificacion.objects.filter(producto=product_id)
    totacal = 0.0
    average = 0.0
    for cal in calificaciones:
        totacal += float(cal.calificacion)
    if totacal:
        average = totacal/len(calificaciones)
    promedio = range(int(average))

    return render(request,"shop-details.html",{"producto":producto,"productos_relacionados":productos_relacionados,"calificaciones":calificaciones,"promedio":promedio})

def shopping_cart(request):
    return render(request,"shoping-cart.html")


def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,"contact.html")


def lista_categorias(request):
    return HttpResponse("lista categorias")
