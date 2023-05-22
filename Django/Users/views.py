from django.shortcuts import render, redirect
from django.contrib import messages
from Management.models import Employee, Vacation
import datetime
from .forms import *

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

def vacation(request, id):
        if request.method == 'POST':
                form = EmployeeVacationForm(request.POST, instance=Employee.objects.get(id=id))
                if form.is_valid():
                        # Check if the employee has enough vacation days
                        # If they do, then create the vacation request
                        # Else, return an error message
                        beginDate = form.cleaned_data.get('startDate')
                        endDate = form.cleaned_data.get('endDate')
                        numDaysDelta = endDate - beginDate
                        numDays = numDaysDelta.days
                        availableVacation = Employee.objects.filter(id = id).values('availableVacation')
                        availableVacation = availableVacation[0]['availableVacation']
                        approvedVacation = Employee.objects.filter(id = id).values('approvedVacation')
                        approvedVacation = approvedVacation[0]['approvedVacation']
                        if (availableVacation < numDays):
                                return render(request, 'Management/vacation.html', {'error': 'Not enough vacation days'})
                        Employee.objects.filter(id = id).update(availableVacation = availableVacation - numDays)
                        Employee.objects.filter(id = id).update(approvedVacation = approvedVacation + numDays)
                        form.save()
                        
        else:
                form = EmployeeVacationForm(instance=Employee.objects.get(id=id))

        return render(request, 'Users/vacation.html', {'form': form, 'id': id})
        if (request.method == 'POST'):
                form_data = request.POST
                print(form_data)
                form_id = form_data['empID']
                format = '%Y-%m-%d'
                form_beginDate = datetime.datetime.strptime(form_data['beginDate'], format) 
                form_endDate = datetime.datetime.strptime(form_data['endDate'], format)
                #the number of days between the start and end date
                numDaysDelta = form_endDate - form_beginDate
                numDays = numDaysDelta.days
                form_reason = form_data['reason']
                # get the employee's available vacation days
                # if the employee has enough days, then create the vacation request
                # else, return an error message
                
                Employee.objects.filter(id = form_id).update(availableVacation = availableVacation - numDays)
                Employee.objects.filter(id = form_id).update(approvedVacation = approvedVacation + numDays)
                VacEmployee = Employee.objects.get(id = form_id)
                Vacation.objects.create(employeeID = VacEmployee, startDate = form_beginDate, endDate = form_endDate, status = 'Pending', reason = form_reason)
                return redirect('hr-vacationList')
        return render(request, 'Users/vacation.html')

def vacationList(request):
        return render(request, 'Management/vacationList.html')
