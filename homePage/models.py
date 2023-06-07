from django.db import models
class Pago(models.Model):
    #key = models.ForeignKey()
    fechaHora = models.DateTimeField()
    celular = models.PositiveIntegerField()
    recibo = models.PositiveBigIntegerField()
    cip = models.PositiveIntegerField()
    pin = models.PositiveIntegerField()
    monto = models.PositiveBigIntegerField()
    confirmado = models.BooleanField()
    sms = models.BooleanField()
    nombre = models.TextField(max_length=40, blank=True, null=True)
    correo = models.TextField(max_length=50, blank=True, null=True)
    dni = models.PositiveIntegerField(blank=True, null=True)
    pregunta1 = models.TextField(max_length= 50, blank=True, null=True)
    pregunta2 = models.TextField(max_length= 50, blank=True, null=True)
    
class Tickets(models.Model):
    ticket = models.PositiveIntegerField()
    cip = models.PositiveIntegerField()
    tipo = models.PositiveIntegerField()
    fechaHora = models.DateTimeField()
    celular = models.PositiveIntegerField()
    recibo = models.PositiveIntegerField()
    pinIntentos = models.PositiveIntegerField()
    confirmado = models.BooleanField()
    nombre = models.TextField(max_length=40, blank=True, null=True)
    correo = models.TextField(max_length=50, blank=True, null=True)
    dni = models.PositiveIntegerField(blank=True, null=True)
    pregunta1 = models.TextField(max_length= 50, blank=True, null=True)
    pregunta2 = models.TextField(max_length= 50, blank=True, null=True)
    
class Tipos(models.Model):
    tipo = models.PositiveIntegerField()
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveBigIntegerField()

class Preguntas(models.Model):
    tipo = models.PositiveIntegerField()
    pregunta = models.CharField(max_length=100)
    def __str__(self):
        return self.pregunta
    
class codigosCelularValidacion(models.Model):
    correlativo      = models.AutoField(primary_key=True)
    celular          = models.CharField(max_length=9)
    codigovalidacion = models.CharField(max_length=50)

    class Meta:
        db_table = 'CelularesyCodigosValidacion'  # Reemplaza 'nombre_de_la_tabla' por el nombre que desees para tu tabla