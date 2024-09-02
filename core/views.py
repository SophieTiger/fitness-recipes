from django.shortcuts import render
from .models import About
from .forms import ContactForm

# Create your views here.
def about_fitness_recipes(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form,
        },
    )