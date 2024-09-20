from django.db import models

# Create your models here.


class About(models.Model):
    """
    Stores a description of the site purpose and the services provided.
    """
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    """
    Stores the info to be filled in the contact request form
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact request from {self.name}"
