from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombres=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=40)
    # Como se vera el dato en el panel de administracion
    # El campo puede ser nulo y en los formularios puede ser vacio 
    fechaNaci=models.DateField(verbose_name='Fecha Nacimiento',null=True,blank=True)
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

class Rentas(models.Model):
    fecha_renta = models.DateField()
    duracion_renta = models.IntegerField()
    fecha_salida = models.DateField()
    fecha_entrega = models.DateField()

    #Relacion 1 a muchos

    autos = models.ForeignKey(Autos, on_delete=models.CASCADE)
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    
    #https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/
    #https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey 

    # Relacion 1 a 1
    #capital= models.OneToOneField(Pais,on_delete=models.CASCADE)
    #https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/

    
    def __str__(self):
        return 'fecha_renta: %s, con duracion_renta: %s, fecha_salida: %s , fecha_entrega: %s' %(self.fecha_renta,self.duracion_renta,self.fecha_salida,self.fecha_entrega)

