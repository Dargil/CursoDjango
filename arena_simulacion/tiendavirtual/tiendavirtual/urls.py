"""tiendavirtual URL Configuration

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
from tiendavirtualapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('listaactivos/<int:cat_prod>/', views.lista_productos),
    path('productodetalles/<int:product_id>/', views.producto_detalles),
    path('listacategorias/', views.lista_categorias),
    path('shoppingcart/', views.shopping_cart),
    path('checkout/', views.checkout),
    path('contact/', views.contact),
    path('resultadobuscador/', views.resultado_buscador),
    path('addproduct', views.add_product),
    path('changeproductquantity', views.changeproductquantity),
    path('deleteproduct', views.deleteproduct)
    
    
    
    


]
