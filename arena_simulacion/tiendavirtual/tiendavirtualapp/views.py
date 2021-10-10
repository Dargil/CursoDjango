from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context,loader
# Create your views here.

def home(request):
    return render(request,"base_template.html")
def lista_productos(request):
    return HttpResponse("lista productos")
def producto_detalles(request,product_id):
    return HttpResponse("Detalle productos")
def lista_categorias(request):
    return HttpResponse("lista categorias")
