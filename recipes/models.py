from django.db import models

class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length = 50)
    #ENUM
    class Dificultad(models.TextChoices):
        FACIL = 'F', _('Facil')
        MEDIA = 'M', _('Media')
        DIFICIL = 'D', _('Dificil')
        def getDificultad(self) -> Dificultad:
            return self.Dificultad(self.dificultad)
    dificultad = models.CharField(
        max_length = 1,
        choices=Dificultad.choices,
        default=Dificultad.MEDIA,
    )
    tiempo_preparacion = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen_url = ImageField(upload_to='images/')





# Create your models here.
