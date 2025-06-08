# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path

from . import views


urlpatterns = [
    path('', views.marketplace_home, name='marketplace_home'),
    path('create', views.marketplace_create, name='marketplace_create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='marketplace_show'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='marketplace_update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='marketplace_delete'),
]
