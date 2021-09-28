from django import forms
from django.db.models import fields
from Rentas.models import Autos

class FormularioAuto2(forms.Form):
    placa = forms.CharField(max_length=7)
    tipo = forms.CharField(max_length=10)
    marca = forms.CharField(max_length=20)
    modelo= forms.IntegerField()
    valor_renta = forms.IntegerField()

class FormularioAuto(forms.ModelForm):
    placa = forms.CharField(max_length=7)
    tipo = forms.CharField(max_length=10)
    marca = forms.CharField(max_length=20)
    modelo= forms.IntegerField()
    valor_renta = forms.IntegerField()

    class Meta:
        model=Autos
        fields = ['placa','tipo','marca','modelo','valor_renta']
