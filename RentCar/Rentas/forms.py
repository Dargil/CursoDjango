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
    placa = forms.CharField(max_length=7, widget=forms.TextInput(attrs={"placeholder":"Por favor ingrese la placa","class":"mi-input"}))
    tipo = forms.CharField(max_length=10)
    marca = forms.CharField(max_length=20)
    modelo= forms.IntegerField()
    valor_renta = forms.IntegerField()

    class Meta:
        model=Autos
        fields = ['placa','tipo','marca','modelo','valor_renta']

# Aplicar validaciones de datos a los datos adicionales del formulario
    def clean_placa(self, *args,**kargs):
        placa=self.cleaned_data.get("placa")
        for letter in placa[0:3]:
            if not letter.isalpha():
                raise forms.ValidationError("No es una placa valida")
        return placa
