from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse

def projects(request):
        return render(request, 'Management/projects.html')

def home(request):
        return render(request, 'Management/index.html')

def about(request):
        return render(request, 'Management/aboutUs.html')

def searchEmployee(request):
        searchTerm = request.GET.get('searchTerm', '')
        
        if searchTerm:
                employees = Employee.objects.filter(empName__icontains=searchTerm)
        else:
                employees = Employee.objects.all()
                
        data = [{'empName': employee.name, 'id': employee.id} for employee in employees]
        return JsonResponse(data, safe=False)