from django.db import models


# Para generar Archivos Unicos como imagenes
import os
import uuid
# Create your models here.


def custom_upload_to_producto(instance, filename):
    """
    Genera un nombre de archivo único basado en un UUID.
    """
    nombre_base, extension = os.path.splitext(filename)
    unique_id = uuid.uuid4().hex
    return f"producto/{unique_id}{extension.lower()}"



class CategoryFood(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


# Create your models here.
class Food(models.Model):
    """
    Modelo para almacenar los alimentos disponibles.
    Cada alimento puede tener muchos gustos asociados de diferentes usuarios.
    """

    name = models.CharField(max_length=100)
    
    # Relación con el tipo de gusto
    category = models.ForeignKey(
        'CategoryFood',  # Relación con el modelo de tipo de gusto
        on_delete=models.CASCADE,
        # Permite acceder a las categorias de un tipo de gusto con `category.foods`
        related_name="foods",  
    )
    
    # Imagen principal del producto, por ahora será unica
    image = models.ImageField(upload_to=custom_upload_to_producto, null=True, blank=True)
    
    # Por ahora solucion viable carga por pinterest
    image_url = models.TextField(null=True, blank=True, 
                                 default="https://i.pinimg.com/736x/32/fd/c3/32fdc305ad5fc48a75e527d0040e51d0.jpg")
    

    # sub_category = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Alimento"
        verbose_name_plural = "Alimentos"