


import pandas as pd
from django.core.management.base import BaseCommand
from users.models import CustomUser
from gustos.models import Favorites, TypeFav
from productos.models import Food, CategoryFood


# No es necesario agregar este comando a ningun lado
# Por el momento solo hay que poner en nuestra terminal
# python manage.py tastes_load

class Command(BaseCommand):
    help = 'Carga usuarios y gustos desde un archivo Excel'

    def handle(self, *args, **kwargs):
        # Ruta al archivo Excel
        file_path = 'gustos/data/gustos_ari.xlsx'
        try:
            df = pd.read_excel(file_path)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Archivo no encontrado: {file_path}'))
            return

        # Crear tipos de gustos si no existen
        tipo_gustos = ["No me gusta", "Ni fu ni fa", "Me gusta"]
        for tipo in tipo_gustos:
            TypeFav.objects.get_or_create(name=tipo)

        for index, row in df.iterrows():
            # Validar y obtener datos del Excel
            name = row.get('name')
            likes = row.get('likes')
            category = row.get('category')
            notes = row.get('Notes')
            user_email = row.get('user')

            if not all([name, likes, category, user_email]):
                self.stdout.write(self.style.WARNING(f'Datos incompletos en la fila {index + 1}. Saltando...'))
                continue

            # Buscar o crear usuario
            user = CustomUser.objects.filter(email=user_email).first()
            if not user:
                self.stdout.write(self.style.WARNING(f'Usuario no encontrado: {user_email}. Saltando...'))
                continue

            # Buscar o crear categoría de comida
            category_obj, _ = CategoryFood.objects.get_or_create(name=category)

            # Buscar o crear comida
            food, _ = Food.objects.get_or_create(name=name, category=category_obj)

            # Buscar tipo de gusto
            type_fav = TypeFav.objects.filter(id=likes).first()
            if not type_fav:
                self.stdout.write(self.style.WARNING(f'Tipo de gusto inválido para "likes": {likes}. Saltando...'))
                continue

            # Verificar si ya existe el gusto
            taste_exists = Favorites.objects.filter(user=user, food=food, type_favs=type_fav).exists()
            if taste_exists:
                self.stdout.write(self.style.WARNING(f'Gusto ya existe para {user.email} y {food.name}. Saltando...'))
                continue

            # Crear el gusto
            Favorites.objects.create(
                user=user,
                food=food,
                note=notes,
                type_favs=type_fav,
            )

            self.stdout.write(self.style.SUCCESS(f'Gusto creado: {user.email} - {food.name}'))
