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
        return 'Cliente %$ %$, fecha Nacimiento: %$, correo: %$' %(self.nombres,self.apellidos,self.fechaNaci,self.correo)

