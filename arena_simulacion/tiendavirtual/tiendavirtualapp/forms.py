from django import forms
from django.db import models
from tiendavirtualapp.models import Clientes,Pedidos

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombres','apellidos','correo','tipo_doc','doc_identificacion','dir_envio','telefono']

class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['forma_pago','valor_total','impuestos','total']