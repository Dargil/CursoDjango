from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombres=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=40)
    fechaNaci=models.DateField()
    cedula=models.IntegerField()
    correo=models.EmailField()
    telefono=models.IntegerField()

    def __str__(self):
        return 'Cliente %s %s, fecha Nacimiento: %s, correo: %s' %(self.nombres,self.apellidos,self.fechaNaci,self.correo)

class Autos(models.Model):
    placa = models.CharField(max_length=7)
    tipo = models.CharField(max_length=10)
    marca = models.CharField(max_length=20)
    modelo= models.IntegerField()
    valor_renta = models.IntegerField()
    def __str__(self):
        return 'Auto de tipo: %s, con placa: %s, marca: %s , modelo: %s' %(self.tipo,self.placa,self.marca,self.modelo)
