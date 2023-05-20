from django.shortcuts import render
from .models import Employee

def projects(request):
        return render(request, 'Management/projects.html')

def home(request):
        return render(request, 'Management/index.html')

def about(request):
        return render(request, 'Management/aboutUs.html')

def data(request):
        return render(request, 'Management/employeeData.html', {'empData': Employee.objects.all()})

def vacation(request):
        return render(request, 'Management/vacation.html')

def vacationList(request):
        return render(request, 'Management/vacationList.html')
