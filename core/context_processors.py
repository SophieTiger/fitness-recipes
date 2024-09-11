from django.urls import reverse

def nav_urls(request):
    return {
        'home_url': reverse('home'),
        'about_url': reverse('about'),
        'recipes_url': reverse('recipes'),
        'favorites_url': reverse('favorites'),
        'logout_url': reverse('account_logout'),
        'signup_url': reverse('account_signup'),
        'login_url': reverse('account_login'),        
    }