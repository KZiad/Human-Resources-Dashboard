from django.shortcuts import render, redirect
from django.contrib import messages
from Management.models import Employee
from .forms import EmployeeRegistrationForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def createEmployee(request):
    
        if request.method == 'POST':
                form = EmployeeRegistrationForm(request.POST)

                if form.is_valid():
                        number = form.cleaned_data.get('number') 
                        if len(number) != 11:
                                messages.error(request, "Please enter a valid phone number")
                                return render(request, 'Users/addEmployees.html', {'form': form})
                        form.save()
                        messages.success(request, "Employee added successfully")
                        return redirect('hr-home')
        else:
                form = EmployeeRegistrationForm()

        return render(request, 'Users/addEmployees.html', {'form': form})

def update(request):
        return render(request, 'Users/update.html')

def data(request):
        return render(request, 'Users/employeeData.html', {'empData': Employee.objects.all()})

def vacation(request):
        return render(request, 'Management/vacation.html')

def vacationList(request):
        return render(request, 'Management/vacationList.html')
