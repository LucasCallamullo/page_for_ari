

from django.urls import path

from home import views

urlpatterns = [
    path('', views.calendar_view, name="Home"),
    
    path('flores/', views.flowers_view, name="Flores"),
]