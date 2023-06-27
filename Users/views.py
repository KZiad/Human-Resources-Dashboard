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
                        dob = form.cleaned_data.get('dob')
                        difference = datetime.date.today() - dob
                        if(difference.days <= 6574.5):
                                messages.warning(request, "Must be at least 18 years old")
                                return render(request, 'Users/addEmployees.html', {'form': form})

                        number = form.cleaned_data.get('number') 
                        if len(number) != 11:
                                messages.warning(request, "Invalid mobile number")
                                return render(request, 'Users/addEmployees.html', {'form': form})
                        
                        vacation = form.cleaned_data.get('availableVacation')
                        if vacation >= 31:
                                messages.warning(request, "Max vacation is 31 days")
                                return render(request, 'Users/addEmployees.html', {'form': form})

                        salary = form.cleaned_data.get('salary')
                        if salary >= 5000_000:
                                messages.warning(request, "Max salary is 500K")
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
                        dob = form.cleaned_data.get('dob')
                        difference = datetime.date.today() - dob
                        if(difference.days <= 6574.5):
                                messages.warning(request, "Must be at least 18 years old")
                                return render(request, 'Users/addEmployees.html', {'form': form})

                        number = form.cleaned_data.get('number') 
                        if len(number) != 11:
                                messages.warning(request, "Invalid mobile number")
                                return render(request, 'Users/addEmployees.html', {'form': form})
                        
                        vacation = form.cleaned_data.get('availableVacation')
                        if vacation >= 31:
                                messages.warning(request, "Max vacation is 31 days")
                                return render(request, 'Users/addEmployees.html', {'form': form})

                        salary = form.cleaned_data.get('salary')
                        if salary >= 5000_000:
                                messages.warning(request, "Max salary is 500K")
                                return render(request, 'Users/addEmployees.html', {'form': form})
                        
                        form.save()
                        messages.info(request, "Employee updated successfully")
                        return redirect('hr-home')
        else:
                form = EmployeeUpdateForm(instance=Employee.objects.get(id=id))

        return render(request, 'Users/update.html', {'form': form, 'id': id})

def delete(request, id):
        Employee.objects.get(id=id).delete()
        messages.error(request, "Employee deleted successfully")
        return redirect('hr-home')

def data(request, id):
        return render(request, 'Users/employeeData.html', {'empData': Employee.objects.get(id=id)})

def vacation(request, id):
        emp = Employee.objects.get(id = id)
        if request.method == 'POST':
                
                form = EmployeeVacationForm(request.POST)
                print(form.errors)
                if form.is_valid():
                        # Check if the employee has enough vacation days
                        # If they do, then create the vacation request
                        # Else, return an error message
                        
                        beginDate = form.cleaned_data.get('startDate')
                        endDate = form.cleaned_data.get('endDate')
                        numDaysDelta = endDate - beginDate
                        numDays = numDaysDelta.days
                        availableVacation = emp.availableVacation
                        approvedVacation = emp.approvedVacation
                        if (availableVacation < numDays):
                                # return error message
                                messages.warning(request, "Employee does not have enough vacation days")
                                form = EmployeeVacationForm(initial={'employeeID': id, 'empname': emp.name, 'startDate': beginDate, 'endDate': endDate, 'reason': form.cleaned_data.get('reason')})
                                return render(request, 'Users/vacation.html', {'form': form, 'availableDays': emp.availableVacation})
                        emp.availableVacation = availableVacation - numDays
                        emp.approvedVacation = approvedVacation + numDays
                        emp.save()
                        # Set the employeeID field to the employee's id
                        # Set the status field to pending

                        form.instance.employeeID = Employee.objects.get(id = id)
                        form.instance.status = 'Pending'

                        form.save()
                        messages.success(request, "Vacation request sent successfully")
                        return redirect('hr-home')
                        
        else:
                # get the employee's name and send it to the form
                employeeName = emp.name
                form = EmployeeVacationForm(initial={'employeeID': id, 'empname': employeeName, 'startDate': datetime.date.today()})

        return render(request, 'Users/vacation.html', {'form': form, 'availableDays': emp.availableVacation})

# poor man's api calls
def deleteVacation(request, id):
        Vacation.objects.get(id=id).delete()
        messages.info(request, "Vacation request deleted successfully")
        return redirect('hr-vacationList')
def approveVacation(request, id):
        vacation = Vacation.objects.get(id=id)
        vacation.status = 'Approved'
        vacation.save()
        messages.success(request, "Vacation request approved successfully")
        return redirect('hr-vacationList')
def denyVacation(request, id):
        vacation = Vacation.objects.get(id=id)
        vacation.status = 'Rejected'
        vacation.save()
        # return the vacation days to the employee
        emp = vacation.employeeID
        numDays = vacation.calculateDays()
        emp.availableVacation = emp.availableVacation + numDays
        emp.approvedVacation = emp.approvedVacation - numDays
        emp.save()
        messages.success(request, "Vacation request rejected successfully")
        return redirect('hr-vacationList')
def vacationList(request):
        vacations = Vacation.objects.all()
        employees = Employee.objects.all()
        return render(request, 'Users/vacationList.html', {'vacs': vacations, 'emps': employees})
