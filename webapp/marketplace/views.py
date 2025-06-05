from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Posts
from .forms import PostsForm

# Create your views here.

def marketplace_home(request):
    posts = Posts.objects.all().order_by('-published_at')
    return render(request, 'marketplace/index.html', {'posts': posts})

@login_required(login_url='/user/login/')
def marketplace_create(request):
    error = ''

    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect('marketplace_home')
        else:
            error = 'Submitted form contain errors'
    else:
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

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    template_name = 'marketplace/update.html'
    form_class = PostsForm
    login_url = '/user/login/'

    def test_func(self):
        post = self.get_object()
        return post.owner == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'marketplace/delete.html'
    success_url = '/marketplace/'
    login_url = '/user/login/'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return post.owner == self.request.user