from django.http import HttpResponse
import datetime
from django.template import Template, Context

# Lectura directa del archivo
def holamundoPlantilla1(request,nombre):
    """Vista Hola Mundo"""
    doc = open ("/home/jefferson/Documents/Curso Django/CursoDjango/prueba1/prueba1/templates/miprimeraplantilla.html")
    plt=Template(doc.read())
    doc.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

# Pasando variables a plantillas mediante contextos
#http://127.0.0.1:8000/hola/oscar
def holamundoPlantilla(request,nombre):
    """Vista Hola Mundo"""
    doc = open ("/home/jefferson/Documents/Curso Django/CursoDjango/prueba1/prueba1/templates/miprimeraplantilla.html")
    plt=Template(doc.read())
    doc.close()
    ctx=Context({"nombre_user":nombre})
    documento=plt.render(ctx)
    return HttpResponse(documento)


# se crea el archvo
# Contenido estatico
# cualquier metodo debe recibir el parametro request
def holamundo2(request):
    """Vista Hola Mundo"""
    return HttpResponse("Bienvenidos al curso de Django")

# forma de enviar la variable http://127.0.0.1:8000/hola/pedro
def holamundo(request,nombre):
    """Vista Hola Mundo"""
    texto="Bienvenido %s al curso de Django "% nombre
    return HttpResponse(texto)

def recibonumero(request,num):
    """Vista para impresión de número"""
    texto="En número recibido es: %s"% num
    return HttpResponse(texto)

#contenido dinamico
# cualquier metodo debe recibir el parametro request
def fecha(request):
    """ Vista para imprimir la fecha"""
    hoy=datetime.datetime.now()
    return HttpResponse(hoy)

# Cómo enviar múltiples parámetros
def division(request,num1,num2):
    """ Vista para dividir dos números"""
    divi=num1/num2
    return HttpResponse("El resultado de la división es: %s" % divi)