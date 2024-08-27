from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipes'),
    path('tag/<slug:tag_slug>/', views.RecipeList.as_view(), name='recipes_list_by_tag'),
]