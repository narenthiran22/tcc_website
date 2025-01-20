from django.urls import path
from . import views

app_name = 'cricket'

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.players, name='players'),
    path('matches/', views.matches, name='matches'),
    path('news/', views.news, name='news'),
]
