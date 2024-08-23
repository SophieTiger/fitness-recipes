from django.db import models
from django.contrib.auth.models import User


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title



