from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipes'),
    path('tag/<slug:tag_slug>/', views.RecipeList.as_view(), name='recipes_list_by_tag'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]