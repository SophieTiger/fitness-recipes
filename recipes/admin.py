from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin
from taggit.forms import TagWidget
from taggit.managers import TaggableManager


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'status', 'created_at', 'get_tags')
    search_fields = ['title', 'ingredients', 'tags__name']
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions')

    formfield_overrides = {
        TaggableManager: {'widget': TagWidget},
    }

    def get_tags(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    get_tags.short_description = 'Tags'


admin.site.register(Comment)
