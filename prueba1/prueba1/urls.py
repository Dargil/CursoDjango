"""prueba1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from prueba1.views import * # se debe importar la view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('holamundo/', holamundo2),
    #identificar un parametro por url
    path('hola2/<nombre>', holamundo),
        #identificar un parametro por url recibir un numero
    path('recibonumero/', recibonumero),


    path('divi/<int:num1>/<int:num2>', division),
    path('hola/<nombre>/<apellido>', holamundoPlantilla),
    path('holarender/<nombre>/<apellido>', holamundo_render),
    path('fecha/', fecha),
]
