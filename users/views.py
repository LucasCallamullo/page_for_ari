

import random
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def profile_view(request):
    return render(request, "users/profile.html")



def frase_linda(request):
    # Función para generar una frase con adjetivos únicos
    
    # Lista extensa de palabras afirmativas y lindas (ordenada alfabéticamente)
    palabras_afirmativas = [
        "adorable", "afable", "agradable", "alegre", "amorosa", "angelical", 
        "apasionada", "auténtica", "bella", "bondadosa", "bonita", 
        "brillante", "carismática", "cariñosa", "chispeante", "clara", 
        "coqueta", "confidente", "creativa", "delicada", "divina", 
        "dulce", "encantadora", "espléndida", "espectacular", 
        "extraordinaria", "fabulosa", "formidable", "fresca", "generosa", 
        "glamorosa", "graciosa", "hermosa", "hipnotizante", "increíble", 
        "inspiradora", "inteligente", "linda", "magnífica", "maravillosa", 
        "mágica", "mía", "noble", "optimista", "perfecta", 
        "positiva", "preciosa", "radiante", "resplandeciente", "romántica", 
        "sabia", "sensacional", "sorprendente", "tierna", "única", 
        "valiente", "valiosa", "virtuosa", 
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



    