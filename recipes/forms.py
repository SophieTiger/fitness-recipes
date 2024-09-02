from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form to allow signed in users to leave a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)