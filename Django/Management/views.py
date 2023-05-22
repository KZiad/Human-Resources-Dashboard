from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse

def projects(request):
        return render(request, 'Management/projects.html')

def home(request):
        employees = Employee.objects.all()     
        return render(request, 'Management/index.html', {'emp': employees})
                

def about(request):
        return render(request, 'Management/aboutUs.html')

def searchEmp(request):
        if request.method == 'GET':
                search_input = request.GET('search-input', '')
                filteredEmp = Employee.objects.filter(name__startswith=search_input)
                serializeEmp = [{'name': emp.name, 'id': emp.id} for emp in filteredEmp]
                return JsonResponse(serializeEmp, safe=False)