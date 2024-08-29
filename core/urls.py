from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_fitness_recipes, name='about'),
]
