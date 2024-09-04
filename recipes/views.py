from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import Recipe, Comment, Like
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

     # Handle comment form submission
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

    # Likes functionality
    likes_count = Like.objects.filter(recipe=recipe).count()
    user_liked = request.user.is_authenticated and Like.objects.filter(
        user=request.user, recipe=recipe).exists()

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "likes_count": likes_count,
        "user_liked": user_liked,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")
    
    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comments
    """
    queryset = Recipe.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
       
    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment Deleted!")
    else:
        messages.add_message(request, messages.ERROR, "It is only possible to delete your own comments!")
    
    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def like_recipe(request, slug):
    """
    View to handle liking/unliking a recipe
    """
    recipe = get_object_or_404(Recipe, slug=slug, status=1)
    like, created = Like.objects.get_or_create(user=request.user, recipe=recipe)

    if not created:
        # If the Like already exists, remove it (unlike)
        like.delete()
        liked = False
    else:
        liked = True
    
    likes_count = Like.objects.filter(recipe=recipe).count()
    return JsonResponse({'liked': liked, 'likes_count': likes_count})

        