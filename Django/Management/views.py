from django.shortcuts import render
from .models import Employee

def projects(request):
        return render(request, 'Management/projects.html')

def home(request):
        return render(request, 'Management/index.html')

def about(request):
        return render(request, 'Management/aboutUs.html')

def data(request):
        context = {
                'empData': Employee.objects.all()
        }
        return render(request, 'Management/employeeData.html', context)

def newEmp(request):
        return render(request, 'Management/addEmployees.html')

def update(request):
        return render(request, 'Management/update.html')

def vacation(request):
        return render(request, 'Management/vacation.html')

def vacationList(request):
        return render(request, 'Management/vacationList.html')
