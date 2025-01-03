from django.urls import path

from users import views

urlpatterns = [
    path('profile/', views.profile_view, name="Profile"),
    
    path('frase_linda/', views.frase_linda, name="frase_linda"),
    
    path('filter_by_likes/', views.filter_by_likes, name="filter_by_likes"),
    
    path('filter_food_category/<int:category_id>/', views.filter_food_category, name='filter_food_category'),
]