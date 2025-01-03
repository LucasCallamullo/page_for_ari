

import random
from django.shortcuts import render
from django.http import JsonResponse

from gustos.models import Favorites
from productos.models import CategoryFood, Food

# Create your views here.
from django.shortcuts import render



def filter_by_likes(request):
    # Filtrar los gustos por correo electrónico del usuario y el tipo de favorito con id=3
    user_favorites = Favorites.objects.filter(user__email='ari@gmail.com', type_favs__id=3)
    
    # Obtener las categorías únicas relacionadas con los gustos del usuario
    categories = CategoryFood.objects.filter(foods__in=user_favorites.values_list('food', flat=True)).distinct()
    
    # Aquí puedes pasar 'user_favorites' al contexto si lo necesitas
    context = {
        'user_favorites': user_favorites,
        'categories': categories,
    }
    
    return render(request, "users/profile.html", context)


def filter_food_category(request, category_id):
    
    # Filtrar los gustos por correo electrónico del usuario
    user_favorites = Favorites.objects.filter(user__email='ari@gmail.com')

    # Obtener las categorías únicas relacionadas con los gustos del usuario
    categories = CategoryFood.objects.filter(foods__in=user_favorites.values_list('food', flat=True)).distinct()

    category = CategoryFood.objects.get(id=category_id)
    
    foods_in_category = Food.objects.filter(category=category)
    
    user_favorites = user_favorites.filter(food__in=foods_in_category)
    
    
    context = {
            'user_favorites': user_favorites,
            'categories': categories,
            'category': category
        }
    
    return render(request, "users/profile.html", context)


def profile_view(request):
    # Filtrar los gustos por correo electrónico del usuario
    user_favorites = Favorites.objects.filter(user__email='ari@gmail.com')

    # Obtener todas las categorías únicas relacionadas con los gustos del usuario
    categories = CategoryFood.objects.filter(foods__in=user_favorites.values_list('food', flat=True)).distinct()

    context = {
        'user_favorites': user_favorites,
        'categories': categories
    }
    
    return render(request, "users/profile.html", context)




def frase_linda(request):
    # Función para generar una frase con adjetivos únicos
    
    # Lista extensa de palabras afirmativas y lindas (ordenada alfabéticamente)
    palabras_afirmativas = [
        "adorable", "agradable", "alegre", "amorosa", "angelical", 
        "apasionada", "auténtica", "bella", "bonita", "brillante", 
        "carismática", "cariñosa", "coqueta", "confidente", "creativa", 
        "delicada", "divina", "dulce", "encantadora", "espectacular", 
        "extraordinaria", "fabulosa", "generosa", "graciosa", "hermosa", 
        "hipnotizante", "increíble", "inspiradora", "inteligente", 
        "linda", "mía", "perfecta", "positiva", "preciosa", "romántica", 
        "sabia", "sorprendente", "tierna", "única", "valiente", "valiosa", 
        "tenes una voz hermosa", "tenes unas tetas hermosas", "tenes unos ojitos hermosos", 
        "tenes un pelo hermoso", "tenes un orto hermoso"
    ]

    lista_temp = palabras_afirmativas.copy()  # Hacemos una copia para no alterar la lista original
    adjetivos = []
    
    for _ in range(5):
        elemento = random.choice(lista_temp)  
        adjetivos.append(elemento)  
        lista_temp.remove(elemento) 
    
    # Construimos la frase
    generated_text = f"Sos {', '.join(adjetivos[:-1])}, y {adjetivos[-1]} yyy Quiero que nunca dudes de que te quiero mucho."

    # Devuelves el texto como una respuesta JSON
    return JsonResponse({'text': generated_text})



    