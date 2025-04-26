# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.marketplace_home, name='marketplace_home'),
    path('create', login_required(views.marketplace_create, login_url='/user/login/'), name='marketplace_create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='marketplace_show'),
    path('<int:pk>/update', login_required(views.PostUpdateView.as_view(), login_url='/user/login/'), name='marketplace_update'),
    path('<int:pk>/delete', login_required(views.PostDeleteView.as_view(), login_url='/user/login/'), name='marketplace_delete'),
]
