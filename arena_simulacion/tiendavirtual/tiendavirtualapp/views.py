from typing import re
from builtins import range
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.template import Template, Context,loader
from tiendavirtualapp.models import Categorias,Clientes,Productos,ProductosPedido,Inventario,Calificacion
# Create your views here.

def home(request):
    validate_session(request)
    # Obtener inicialmente las categorias
    all_cat = Categorias.objects.all().order_by('id')
    # si pongo un signo menos lo ordena de forma descendente
    latest_prod = Productos.objects.all().order_by('-id')[:6]
    # Ordenar los productos por calificacion 
    top_prod = Calificacion.objects.all().order_by('-calificacion')[:6]
    latest_review = Calificacion.objects.all().order_by('-id')[:6]
    return render(request,"home.html",{"all_cat":all_cat,"latest_prod":latest_prod,"top_prod":top_prod,"latest_review":latest_review})

def lista_productos(request,cat_prod):
    validate_session(request)
    if cat_prod == 0:
        productos = Productos.objects.all().order_by('-id')
        categoria = "Todas las categorias"
    else:
        productos = get_list_or_404(Productos,categoria_id=cat_prod)
        categoria_obj = get_object_or_404(Categorias, pk=cat_prod)
        categoria = categoria_obj.nombre
    
    latest_prod = Productos.objects.all().order_by('-id')[:6]

    return render(request,"shop-grid.html",{"productos":productos,"latest_prod":latest_prod,"categoria":categoria})

def producto_detalles(request,product_id):
    validate_session(request)
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
    validate_session(request)
    shopping_list = []
    for product_id, quantity in request.session["shop_cart"]['productos'].items():
        producto = get_object_or_404(Productos,pk=int(product_id))
        total_producto = float(producto.precio_unidad)*quantity
        shopping_list.append({"quantity":quantity,"product_id":product_id,"nombre":producto.nombre,"precio":producto.precio_unidad,"total":total_producto})
    return render(request,"shoping-cart.html",{"shopping_list":shopping_list})


def checkout(request):
    validate_session(request)
    return render(request,"checkout.html")

def contact(request):
    validate_session(request)
    return render(request,"contact.html")


def lista_categorias(request):
    validate_session(request)
    return HttpResponse("lista categorias")


def resultado_buscador(request):
    validate_session(request)
    if request.GET["text"]:
        productos = Productos.objects.filter(nombre__icontains=request.GET["text"])
    else:
        productos = Productos.objects.all().order_by('-id')
    latest_prod = Productos.objects.all().order_by('-id')[:6]
    return render(request, "shop-grid-buscar.html", {"productos":productos,"latest_prod":latest_prod})

def validate_session(request):
    if 'shop_cart' not in request.session:
        request.session["shop_cart"] = {'total_productos':0,'total_valor':0.0,'productos':{}}

def add_product(request):
    if request.POST["product_id"] and request.POST["quantity"]:
        product_id = request.POST["product_id"]
        producto = get_object_or_404(Productos, pk=product_id)
        validate_session(request)

        if str(product_id) in request.session["shop_cart"]:
            request.session["shop_cart"]["productos"][str(product_id)] += int(request.POST["quantity"])
        else:
            request.session["shop_cart"]["productos"][str(product_id)] = int(request.POST["quantity"])
        
        request.session["shop_cart"]["total_productos"] += int(request.POST["quantity"])
        total_val = (producto.precio_unidad * int(request.POST["quantity"]))
        request.session["shop_cart"]["total_valor"] += float(total_val)

        request.session.modified = True
        return HttpResponseRedirect('productodetalles/'+product_id)
    else:
        return HttpResponse('Error no se ha seleccionado un producto')