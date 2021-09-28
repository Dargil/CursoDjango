#from RentCar.Rentas.forms import FormularioAuto
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from Rentas.models import Autos
from Rentas.forms import FormularioAuto

# Create your views here.
def busca_autos_placa(request):
    return render(request,"buscar_autos.html")


#def results_buscar_auto(request):
#    if request.GET["placa"]:
#        placa = request.GET["placa"]
#        autos_busqueda = Autos.objects.get(placa=placa)
#        return render(request,"respuesta_buscar_autos.html",{"autos":autos_busqueda,"placa":placa})
#    else:
#        return HttpResponse("Campo placa no diligenciado")


def results_buscar_auto(request):
    if request.POST["placa"]:
        placa = request.POST["placa"]
        autos_busqueda = Autos.objects.filter(placa__icontains=placa)
        return render(request,"respuesta_buscar_autos.html",{"autos":autos_busqueda,"placa":placa})
    else:
        return HttpResponse("Campo placa no diligenciado")

#https://docs.djangoproject.com/en/3.2/ref/forms/api/


def crear_auto2(request):
    if(request.method=='POST'):
        miform = FormularioAuto(request.POST)

        if miform.is_valid():
            datos = miform.cleaned_data
            new_auto = Autos(placa=datos['placa'],tipo=datos['tipo'],marca=datos['marca'],modelo=datos['modelo'],valor_renta=datos['valor_renta'])
            new_auto.save()

            return HttpResponse("Nuevo auto fue almacenado correctamente")
    else:
        miform = FormularioAuto()
    return render(request,"nuevo_auto.html",{"form":miform})
 


def crear_auto(request):
    if(request.method=='POST'):
        miform = FormularioAuto(request.POST)

        if miform.is_valid():
            miform.save()
            return HttpResponse("Nuevo auto fue almacenado correctamente")
    else:
        miform = FormularioAuto()
    return render(request,"nuevo_auto.html",{"form":miform})