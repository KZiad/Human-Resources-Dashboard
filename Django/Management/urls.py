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
    path('deleteUser/<id>/', userViews.delete, name='hr-deleteData'),
    path('vacations/<id>/', userViews.vacation, name='hr-vacation'),
    path('vacationList/', userViews.vacationList, name='hr-vacationList'),
    path('deleteVacation/<id>/', userViews.deleteVacation, name='hr-deleteVacation'),
    path('approveVacation/<id>/', userViews.approveVacation, name='hr-approveVacation'),
    path('denyVacation/<id>/', userViews.denyVacation, name='hr-denyVacation'),
]