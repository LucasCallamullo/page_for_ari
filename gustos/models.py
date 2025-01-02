from django.db import models

# Create your models here.


class TypeFav(models.Model):
    """
    Modelo para almacenar los diferentes tipos de gusto.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Gusto"
        verbose_name_plural = "Tipos de Gustos"


class Favorites(models.Model):
    """
    Modelo para almacenar los gustos de los usuarios sobre diferentes alimentos.
    Cada usuario puede tener varios gustos asociados a alimentos específicos.
    """

    # Relación con el usuario (CustomUser)
    user = models.ForeignKey(
        'users.CustomUser',  # Nombre del modelo de usuario personalizado
        on_delete=models.CASCADE,  # Si el usuario se elimina, también se eliminan los gustos asociados
        related_name="favs",  # Permite acceder a los gustos desde el usuario con `user.favs`
    )

    # Relación con los alimentos
    food = models.ForeignKey(
        'productos.Food',  # Nombre del modelo de alimento
        on_delete=models.CASCADE,
        related_name="favs",  # Permite acceder a los gustos de un alimento con `food.favs`
    )

    # Relación con el tipo de gusto
    type_favs = models.ForeignKey(
        'TypeFav',  # Relación con el modelo de tipo de gusto
        on_delete=models.CASCADE,
        related_name="favs",  # Permite acceder a los gustos de un tipo de gusto con `tipo_gusto.favs`
    )

    # Fecha de registro del gusto
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    # Fecha del último intento de prueba o verificación del gusto
    # fecha_last_proof = models.DateTimeField(auto_now=True)

    # Estrellas (valoración del gusto)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)
    
    # Nota adicional sobre el gusto
    note = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.user.email} - {self.food.name} - {self.type_favs.name} - {self.stars}"

    class Meta:
        verbose_name = "Gusto"
        verbose_name_plural = "Gustos"