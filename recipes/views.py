from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm
from taggit.models import Tag


class RecipeList(generic.ListView):
    """
    Returns a List of recipes with tags from the database
    """
    model = Recipe
    queryset = Recipe.objects.all()
    template_name = "recipe_list.html"
    context_object_name = 'recipes'
    paginate_by = 9

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


def recipe_detail(request, slug):
    """
    Display an individual :model:`recipes.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipes.Recipe`.

    **Template:**

    :template:`recipes/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for the comment, it is submitted and pending approval'
            )
    
    comment_form = CommentForm()

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )