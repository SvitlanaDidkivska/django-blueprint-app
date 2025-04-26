from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required 

from .models import Posts
from .forms import PostsForm

# Create your views here.

def marketplace_home(request):
    posts = Posts.objects.all().order_by('-published_at')
    return render(request, 'marketplace/index.html', {'posts': posts})

def marketplace_create(request):
    error = ''

    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketplace_home')
        else:
            error = 'Submitted form contain errors'

    form = PostsForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'marketplace/create.html', data)

class PostDetailView(DetailView):
    model = Posts
    template_name = 'marketplace/show.html'
    context_object_name = 'post'

class PostUpdateView(UpdateView):
    model = Posts
    template_name = 'marketplace/update.html'
    form_class = PostsForm

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'marketplace/delete.html'
    success_url = '/marketplace/'