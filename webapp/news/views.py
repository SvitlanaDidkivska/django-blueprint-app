from django.shortcuts import render
from django.views.generic import DetailView

from .models import News

# Create your views here.

def news_home(request):
    news = News.objects.all().order_by('-published_at')
    return render(request, 'news/index.html', {'newses': news})

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/show.html'
    context_object_name = 'news'