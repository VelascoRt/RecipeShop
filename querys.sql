USE recipes;
GO
SELECT * FROM recipes_receta;

INSERT INTO recipes_receta(titulo,descripcion,categoria,dificultad,tiempo_preparacion,precio,imagen_url,es_premium) VALUES 
("Postre De Crema De Bayas",
"Este postre no solo tiene una presentación muy bonita, lo más importante es que está cargado con antioxidantes, fibra y proteína. Es también una perfecta opción para el desayuno, con 20 gramos de carbohidratos y 14 gramos de azúcar.",
"Postre",
"Media",
2500,
45.00,
"https://images.pexels.com/photos/414262/pexels-photo-414262.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
true
);
/*
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
    imagen_url = models.ImageField(upload_to='images/')
    es_premium = models.BooleanField()
*/
