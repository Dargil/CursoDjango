from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def busca_autos_placa(request):
    return render(request,"buscar_autos.html")


def results_buscar_auto(request):
    respuesta = "Buscando auto con placa : %s " % request.GET["placa"]

    return HttpResponse(respuesta)
