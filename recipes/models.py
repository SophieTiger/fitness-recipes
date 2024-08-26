from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


SERVINGS = [tuple([x, x]) for x in range(1, 11)]
STATUS = ((0, "Draft"), (1, "Published"))

class Recipe(models.Model):
    """
    Stores a Recipe post entered by admin related to :model:`auth.User`.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
        limit_choices_to={'is_staff': True}, related_name="recipe_posts")
    servings = models.IntegerField(choices=SERVINGS)
    calories = models.CharField(max_length=10)
    protein = models.CharField(max_length=10)
    carbs = models.CharField(max_length=10)
    fat = models.CharField(max_length=10)
    ingredients = models.TextField()
    instructions = models.TextField()
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Stores a single comment made to a Recipe post related to :model: `recipes.recipe`
    and :model:`auth.User`
    """
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} written by {self.author}"



