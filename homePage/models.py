from django.db import models
class Pago(models.Model):
    key = models.ForeignKey()
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
    monto = models.PositiveIntegerField()

class Preguntas(models.Model):
    tipo = models.PositiveIntegerField()
    pregunta = models.TextField()
    def __str__(self):
        return self.pregunta