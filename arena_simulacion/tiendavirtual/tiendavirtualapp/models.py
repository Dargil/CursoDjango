from django.db import models
import datetime
# Create your models here.

class Categorias(models.Model):
    codigo = models.CharField(max_length=5,verbose_name='Código de la Categoría')
    nombre = models.CharField(max_length=20,verbose_name='Nombre de la Categoría')
    descripcion = models.TextField(verbose_name='Texto descriptivo de la Categoría')
    TRUE_FALSE_CHOISES = (
        ('Si','Activo'),
        ('No','Inactivo')
    )
    activo = models.CharField(max_length=2,choices=TRUE_FALSE_CHOISES,default='Si')

    def __str__(self):
        return 'Categoria: %s, con código: %s, activa: %s' % (self.nombre,self.codigo,self.activo)
    class Meta:
        verbose_name_plural = "Categorias"

class Productos(models.Model):
    codigo = models.CharField(max_length=5,verbose_name='Código del producto')
    nombre = models.CharField(max_length=20,verbose_name='Nombre del producto')
    descripcion = models.TextField(verbose_name='Texto descriptivo del producto')
    UNIDAD_CHOISES = (
        ('Kg','Kilogramo'),
        ('Lb','Libra'),
        ('Un','Unidad'),
        ('Pa','Paquete')
    )
    unidad = models.CharField(max_length=2,choices=UNIDAD_CHOISES,default='Kg')
    fecha_registro = models.DateField(default=datetime.date.today)
    precio_unidad = models.DecimalField(decimal_places=2,max_digits=10)
    fecha_precio = models.DateField(default=datetime.date.today)
    imagen = models.CharField(max_length=100,null=True,blank=True)
    TRUE_FALSE_CHOISES = (
            ('Si','Activo'),
            ('No','Inactivo')
        )
    activo = models.CharField(max_length=2,choices=TRUE_FALSE_CHOISES,default='Si')

    #Relacion 1 a Muchos
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)

    def __str__(self):
        return 'Producto: %s, con código: %s, activo: %s, precio: %s' % (self.nombre,self.codigo,self.activo,self.precio_unidad)
    class Meta:
        verbose_name_plural = "Productos"

class Clientes(models.Model):
    nombres = models.CharField(max_length=20,verbose_name='Nombres')
    apellidos = models.CharField(max_length=20,verbose_name='Apellidos')
    correo = models.EmailField(verbose_name='Correo electrónico')
    DOC_CHOISES = (
        ('Cc','Cédula'),
        ('Pa','Pasaporte'),
        ('Ce','Cédula Extranjería')
    )
    tipo_doc = models.CharField(max_length=2,choices=DOC_CHOISES,default='Cc',verbose_name='Tipo Doc. Identificación')
    doc_identificacion = models.CharField(max_length=15,verbose_name='Documento Identificación')
    dir_envio = models.CharField(max_length=100,verbose_name='Dirección de Envio')
    fecha_registro = models.DateField(default=datetime.date.today)
    TRUE_FALSE_CHOISES = (
        ('Si','Activo'),
        ('No','Inactivo')
    )
    activo = models.CharField(max_length=2,choices=TRUE_FALSE_CHOISES,default='Si')
    #Se habia olvidado especificar este atributo
    telefono = models.CharField(max_length=15,verbose_name='Teléfono')
    def __str__(self):
        return 'Cliente: %s, con dirección: %s, correo: %s, fecha registro: %s' % (self.nombres,self.dir_envio,self.correo,self.fecha_registro)

    class Meta:
        verbose_name_plural = "Clientes"


class Pedidos(models.Model):
    fecha_pedido = models.DateField(default=datetime.date.today)
    PAGO_CHOISES = (
        ('PSE','PSE'),
        ('Tj','Tarjeta Crédito'),
        ('Py','Paypal'),
        ('Mp','Mercado Pago')
    )
    forma_pago = models.CharField(max_length=3,choices=PAGO_CHOISES,default='PSE')
    valor_total = models.DecimalField(decimal_places=2,max_digits=15)
    impuestos = models.DecimalField(decimal_places=2,max_digits=15)
    total = models.DecimalField(decimal_places=2,max_digits=15)

    ESTADO_CHOISES = (
        ('Rg','Registrado'),
        ('Pr','En preparación'),
        ('En','Enviado'),
        ('Re','Recibio Cliente'),
        ('Fn','Finalizado sin reclamaciones'),
        ('Fr','Finalizado con reclamaciones'),
        ('Ca','Cancelado')
    )
    estado = models.CharField(max_length=2,choices=ESTADO_CHOISES,default='Rg')
    
    # Se habia olvidado ingresar esta relacion
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = "Pedidos"

class ProductosPedido(models.Model):
    #Relacion 1 a Muchos
    pedido = models.ForeignKey(Pedidos,on_delete=models.PROTECT)
    Productos = models.ForeignKey(Productos,on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(decimal_places=2,max_digits=10)

class Inventario(models.Model):
    BODEGA_CHOISES = (
        ('CeB','Bodega Centro Cr 3b 12-23 Bog'),
        ('SuB','Bodega Sur calle 34c 14-13 Bog'),
        ('NoB','Bodega Norte Calle 80 64-23 Bog')
    )
    producto = models.OneToOneField(Productos, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=3,choices=BODEGA_CHOISES,default='NoB')
    precio_entrada = models.DecimalField(decimal_places=2,max_digits=10)
    fecha_registro = models.DateField(default=datetime.date.today)

    def __str__(self):
        return 'Inventario: %s, cantidad: %s, ubicacion: %s' % (self.producto.nombre,self.cantidad,self.ubicacion)
    


class Calificacion(models.Model):
    CAL_CHOISES = (
        ('1','[1] Estrella'),
        ('2','[2] Estrella'),
        ('3','[3] Estrella'),
        ('4','[4] Estrella'),
        ('5','[5] Estrella')
    )

    calificacion = models.CharField(max_length=1,choices=CAL_CHOISES,default='5')
    fecha_calificacion = models.DateField(default=datetime.date.today)
    comentario = models.TextField()
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)

    def __str__(self):
        return 'calificacion: %s %s, fecha: %s' % (self.producto.codigo,self.calificacion,self.fecha_calificacion)
   

    class Meta:
        verbose_name_plural = 'Calificaciones'
