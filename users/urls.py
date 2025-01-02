from django.urls import path

from users import views

urlpatterns = [
    path('profile/', views.profile_view, name="Profile"),
    
    path('frase_linda/', views.frase_linda, name="frase_linda"),
]