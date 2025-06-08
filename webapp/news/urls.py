from django.urls import path

from . import views # from current folder import the neighbour file views for views methods usage

urlpatterns = [
    path('', views.news_home, name ='news_home'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_show'),
]
 