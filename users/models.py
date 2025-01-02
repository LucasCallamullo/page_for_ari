
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

import os
import uuid


def custom_upload_to_registro(instance, filename):
    # Función para generar un nombre de archivo único basado en un UUID
    # Esto se guarda en la direccion media/return(registros/1223asda344.jpg)
    
    nombre_base, extension = os.path.splitext(filename)
    unique_id = uuid.uuid4().hex
    return f"registros/{unique_id}{extension.lower()}"


# Gestor personalizado para manejar la creación de usuarios
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
    
class CustomUser(AbstractUser):
    """
        Modelo para generar un nuevo usuario autenticado con distintos roles, este modelo
        "CustomUser" de momento lo voy a utilizar como una base clase padre para los dos roles
        
        # Estos campos vienen por defecto en el base user
        # =================================================================================
        # first_name = Nombre del comprador
        # last_name = Apellido del usuario
        # last_login: Fecha y hora del último inicio de sesión (actualizable automáticamente).
        # date_joined: Fecha y hora en que se creó la cuenta.
    """
    
    # Elimina el campo de nombre de usuario del modelo de usuario por defecto
    username = None  
    
    # Agrega un campo de correo electrónico único para la autenticación
    email = models.EmailField(unique=True)
    
    # Campos adicionales para el perfil del usuario
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    # address = models.CharField(max_length=255, blank=True, null=True)
    # province = models.CharField(max_length=50, blank=True, null=True)
    # Campo para definir el rol del usuario, por ahora voy a usar el superuser
    # role = models.CharField(max_length=10, default='admin')
    

    # Imagen perfil averiguar si se puede con imagenes estaticas o solo url
    image = models.ImageField(upload_to=custom_upload_to_registro, null=True, blank=True, 
        default="register_users/profile_def.jpg")
    
    image_url = models.TextField(null=True, blank=True, 
        default="https://i.pinimg.com/564x/20/05/e2/2005e27a39fa5f6d97b2e0a95233b2be.jpg")
    
    # Imagen banner del proveedor/comprador si necesitara
    banner_image = models.ImageField(upload_to=custom_upload_to_registro, null=True, blank=True, 
        default="register_users/banner_def.jpg")
    
    banner_image_url = models.TextField(null=True, blank=True, 
        default="https://i.pinimg.com/564x/cb/be/53/cbbe53813cb8c0c85ddeda0d23de874d.jpg")

    # Define el campo email como el nombre de usuario para la autenticación
    USERNAME_FIELD = "email"

    # No se requieren campos adicionales al crear un superusuario
    REQUIRED_FIELDS = []
    
    # Usa el gestor personalizado para este modelo, y lo heredaran sus clases
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"



# Tabla de link url social
class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        # Agrega más plataformas según sea necesario
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.user.username} - {self.platform}"
