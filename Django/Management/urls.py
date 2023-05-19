from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('data/', views.data, name='data'),
]