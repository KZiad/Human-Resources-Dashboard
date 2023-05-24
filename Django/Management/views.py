from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse
import json
def projects(request):
        return render(request, 'Management/projects.html')

def home(request):
        employees = Employee.objects.all()
        return render(request, 'Management/index.html', {'emp': employees})
                

def about(request):
        return render(request, 'Management/aboutUs.html')

def searchEmp(request):
        if request.method == 'POST':
                search_query = json.loads(request.body).get('searchText')
                
                employees = Employee.objects.filter(name__istartswith=search_query)
                data = employees.values()
                return JsonResponse(list(data), safe=False)
