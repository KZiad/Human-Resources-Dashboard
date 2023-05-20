from django.urls import path
from . import views
from Users import views as userViews

urlpatterns = [
    path('', views.projects, name='hr-projects'),
    path('home/', views.home, name='hr-home'),
    path('about/', views.about, name='hr-about'),
    path('data/', views.data, name='hr-data'),
    path('addEmployee/', userViews.createEmployee , name='hr-addEmployee'),
    path('updateData/', userViews.update, name='hr-updateData'),
    path('vacations/', views.vacation, name='hr-vacation'),
    path('vacationList/', views.vacationList, name='hr-vacationList'),
]