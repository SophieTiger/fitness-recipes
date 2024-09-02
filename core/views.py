from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm


# Create your views here.
def about_fitness_recipes(request):
    """
    Renders the About page and Contact form
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for the message! I will get back to you within 24 hours.')

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