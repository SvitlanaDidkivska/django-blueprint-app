from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from marketplace.models import Posts


class PostListView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'dashboard/index.html'
    login_url = '/user/login/'

    def get_queryset(self):
        return Posts.objects.filter(owner=self.request.user).order_by('-published_at')