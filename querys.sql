USE recipes;
GO
SELECT * FROM recipes_receta;

INSERT INTO recipes_receta(titulo,descripcion,categoria,dificultad,tiempo_preparacion,precio,imagen_url,es_premium) VALUES 
("Cupcake integral Con Toppings De Fresa Roja",
"El término cupcake fue recogido por primera vez en el recetario de Eliza Leslie, Seventy-five Recipes for Pastry, Cakes, and Sweetmeats, publicado en 1828. La autora se refería a él como una tartaleta que se cocina en pequeñas tazas, aunque la imagen que acompañaba la receta coincidía con la que actualmente se conoce a este delicioso dulce: un pequeño bizcocho redondo - muy parecido a una magdalena- con una cubierta colorida y cremosa. Sobre el origen del nombre hay dos versiones, la primera versión es que se le dió el nombre porque se horneaban en tazas de barro individuales (taza es cup en inglés), la segunda versión sobre el origen del nombre lo vincula a la forma de calcular los ingredientes empleados en su elaboración (mantequilla, azúcar, huevos, levadura y harina) que se median por tazas.",
"Postre",
"Fácil",
30,
0,
"https://images.pexels.com/photos/1055272/pexels-photo-1055272.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
false
),
("Espaguetti a la boloñesa",
"Esta deliciosa salsa roja, combina carne molida, zanahorias, apio, cebolla, tomates, y con un toque de leche para darle cremosidad. Esta salsa se cocina a fuego lento y se sirve deliciosamente sobre su pasta favorita.",
"Platillo fuerte",
"Media",
15,
0,
"https://images.pexels.com/photos/28575312/pexels-photo-28575312/free-photo-of-espaguetis-a-la-bolonesa-tradicionales-con-ingredientes-frescos.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
true);
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
