from django.shortcuts import render
from django.views import generic
from .models import Recipe
from taggit.models import Tag


class RecipeList(generic.ListView):
    """
    Returns a List of recipes with tags from the database
    """
    model = Recipe
    queryset = Recipe.objects.all()
    template_name = "recipe_list.html"
    context_object_name = 'recipes'
    paginate_by = 6

    def get_queryset(self):
        """
        Filter recipes by tag when a tag_slug is provided in the URL
        """
        queryset = super().get_queryset()
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            tag = Tag.objects.get(slug=tag_slug)
            queryset = queryset.filter(tags__in=[tag])
        return queryset
    
    def get_context_data(self, **kwargs):
        """
        Include all tags in the context, which will allow
        to display a list of all available tags in the template.
        """
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context