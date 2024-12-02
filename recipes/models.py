from django.db import models
from django.contrib.auth.models import User


class Receta(models.Model):
    titulo = models.CharField(max_length = 200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length = 50)
    #ENUM
    class Dificultad(models.TextChoices):
        FACIL = 'Fácil'
        MEDIA = 'Media'
        DIFICIL = 'Díficil'
        def getDificultad(self):
            return self.Dificultad(self.dificultad)
    dificultad = models.CharField(
        max_length = 8,
        choices=Dificultad.choices,
        default=Dificultad.MEDIA,
    )
    tiempo_preparacion = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen_url = models.CharField(max_length= 1500)
    es_premium = models.BooleanField()

class Compra(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")
    receta_id = models.ForeignKey(Receta,on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=6,decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    class MetodoPago(models.TextChoices):
        PAYPAL = 'Paypal'
        VISA = 'Visa'
        MASTERCARD = 'Mastercard'
        AMERICAN_EXPRESS = 'American express'
        def getMetodoPago(self):
            return self.MetodoPago(self.metodo_pago)
    metodo_pago = models.CharField(
        max_length = 20,
        choices = MetodoPago.choices,
        default = MetodoPago.VISA,
    )

# class MetodoPago(Models.Model):
    # nombre = models.CharField(max_length=25)
"""
class Pago(models.Model):
    compra_id = models.ForeignKey(Compra,on_delete=models.CASCADE)
    class MetodoPago(models.TextChoices):
        PAYPAL = 'Paypal'
        VISA = 'Visa'
        MASTERCARD = 'Mastercard'
        AMERICAN_EXPRESS = 'American express'
        def getMetodoPago(self):
            return self.MetodoPago(self.metodo_pago)
    metodo_pago = models.CharField(
        max_length = 20,
        choices = MetodoPago.choices,
        default = MetodoPago.VISA,
    )
"""
