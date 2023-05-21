from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from Management.models import Employee

# Create your views here.

def createEmployee(request):
    if request.method == 'POST':
        form_data = request.POST

        form_name = form_data['name']
        form_id = form_data['id']
        form_email = form_data['email']
        form_address = form_data['address']
        form_number = form_data['number']
        form_gender = form_data['gender']
        form_dob = form_data['dob']
        form_status = form_data['status']
        form_vacation = form_data['vacation']
        form_salary = form_data['salary']

        Employee.objects.create(id = form_id, name = form_name, email = form_email, address = form_address, mobile = form_number, gender = form_gender,
                                status = form_status, availableVacation = form_vacation, approvedVacation = 0, dob = form_dob, salary = form_salary)
        return redirect('hr-home')
    
    return render(request, 'Users/addEmployees.html')

def update(request):
        return render(request, 'Users/update.html')

def data(request):
        return render(request, 'Users/employeeData.html', {'empData': Employee.objects.all()})

def vacation(request):
        return render(request, 'Management/vacation.html')

def vacationList(request):
        return render(request, 'Management/vacationList.html')
