from django.shortcuts import render, redirect
from django.contrib import messages
from Management.models import Employee
from .forms import EmployeeRegistrationForm, EmployeeUpdateForm

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

def update(request, id):
        if request.method == 'POST':
                form = EmployeeUpdateForm(request.POST, instance=Employee.objects.get(id=id))
                if form.is_valid():
                        number = form.cleaned_data.get('number') 
                        if len(number) != 11:
                                messages.error(request, "Please enter a valid phone number")
                                return render(request, 'Users/update.html', {'form': form})
                        form.save()
                        messages.info(request, "Employee updated successfully")
                        return redirect('hr-home')
        else:
                form = EmployeeUpdateForm(instance=Employee.objects.get(id=id))

        return render(request, 'Users/update.html', {'form': form, 'id': id})

def delete(request, id):
        Employee.objects.get(id=id).delete()
        messages.info(request, "Employee deleted successfully")
        return redirect('hr-home')

def data(request, id):
        return render(request, 'Users/employeeData.html', {'empData': Employee.objects.get(id=id)})

def vacation(request):
        return render(request, 'Management/vacation.html')

def vacationList(request):
        return render(request, 'Management/vacationList.html')
