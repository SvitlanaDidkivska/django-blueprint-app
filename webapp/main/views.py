# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.shortcuts import render
from marketplace.models import Posts

# Create your views here.
def index(request):
    posts = Posts.objects.all().order_by('-published_at')[:3]
    return render(request, 'main/index.html', {'posts': posts})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def terms_of_service(request):
    return render(request, 'main/terms-of-service.html')