from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from Management.models import Employee

# Create your views here.

def createEmployee(request):
    if request.method == 'POST':
           form_name = request.POST.get('name')
           form_id = request.POST.get('id')
           form_email = request.POST.get('email')
           form_address = request.POST.get('address')
           form_number = request.POST.get('number')
           form_gender = request.POST.get('gender')
           form_dob = request.POST.get('dob')
           form_status = request.POST.get('status')
           form_vacation = request.POST.get('vacation')
           form_salary = request.POST.get('salary')
           Employee.objects.create(id = form_id, name = form_name, email = form_email, address = form_address, mobile = form_number, gender = form_gender,
                                    status = form_status, availableVacation = form_vacation, approvedVacation = 0, dob = form_dob, salary = form_salary)
           return redirect('hr-home')
    return render(request, 'Users/addEmployees.html')

def update(request):
        return render(request, 'Users/update.html')