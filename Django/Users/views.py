from django.shortcuts import render, redirect
from django.contrib import messages
from Management.models import Employee, Vacation
import datetime
from .forms import EmployeeRegistrationForm, EmployeeUpdateForm

# Create your views here.

def createEmployee(request):
    if request.method == 'POST':
           form_data = request.POST
           print(form_data)
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

def delete(request, id):
        Employee.objects.get(id=id).delete()
        messages.info(request, "Employee deleted successfully")
        return redirect('hr-home')

def data(request, id):
        return render(request, 'Users/employeeData.html', {'empData': Employee.objects.get(id=id)})

def vacation(request, id):
        if (request.method == 'POST'):
                form_data = request.POST
                print(form_data)
                form_id = form_data['empID']
                format = '%Y-%m-%d'
                form_beginDate = datetime.datetime.strptime(form_data['beginDate'], format) 
                form_endDate = datetime.datetime.strptime(form_data['endDate'], format)
                #the number of days between the start and end date
                numDays = form_endDate - form_beginDate
                numDays = numDays.days
                print(numDays)
                form_reason = form_data['reason']
                # get the employee's available vacation days
                # if the employee has enough days, then create the vacation request
                # else, return an error message
                
                availableVacation = Employee.objects.filter(id = form_id).values('availableVacation')
                print(availableVacation)
                availableVacation = availableVacation[0]['availableVacation']
                approvedVacation = Employee.objects.filter(id = form_id).values('approvedVacation')
                approvedVacation = approvedVacation[0]['approvedVacation']
                if (availableVacation < numDays):
                        return render(request, 'Management/vacation.html', {'error': 'Not enough vacation days'})
                Employee.objects.filter(id = form_id).update(availableVacation = availableVacation - numDays)
                Employee.objects.filter(id = form_id).update(approvedVacation = approvedVacation + numDays)
                VacEmployee = Employee.objects.get(id = form_id)
                Vacation.objects.create(employeeID = VacEmployee, startDate = form_beginDate, endDate = form_endDate, status = 'Pending', reason = form_reason)
                return redirect('hr-vacationList')
        return render(request, 'Users/vacation.html')

def vacationList(request):
        return render(request, 'Management/vacationList.html')
