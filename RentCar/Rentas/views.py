from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from Rentas.models import Autos

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
