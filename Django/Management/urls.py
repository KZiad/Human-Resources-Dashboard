from django.urls import path
from . import views
from Users import views as userViews

urlpatterns = [
    path('', views.projects, name='hr-projects'),
    path('home/', views.home, name='hr-home'),
    path('about/', views.about, name='hr-about'),
    path('data/<id>/', userViews.data, name='hr-data'),
    path('addEmployee/', userViews.createEmployee , name='hr-addEmployee'),
    path('updateData/<id>/', userViews.update, name='hr-updateData'),
    path('vacations/', userViews.vacation, name='hr-vacation'),
    path('vacationList/', userViews.vacationList, name='hr-vacationList'),
]