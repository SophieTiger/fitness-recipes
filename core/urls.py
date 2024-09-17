from django.urls import path
from . import views
from .views import Index


urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('about/', views.about_fitness_recipes, name='about'),
    # path('test-500/', views.test_500, name='test_500'),
]
