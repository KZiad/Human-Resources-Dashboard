from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from Management.models import Employee

# Create your views here.

def createEmployee(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
           name = form.cleaned_data.get('name')
           id = form.cleaned_data.get('id')
           email = form.cleaned_data.get('email')
           address = form.cleaned_data.get('address')
           number = form.cleaned_data.get('number')
           gender = form.cleaned_data.get('gender')
           dob = form.cleaned_data.get('dob')
           status = form.cleaned_data.get('status')
           vacation = form.cleaned_data.get('vacation')
           salary = form.cleaned_data.get('salary')
           Employee.objects.create(id = id, name = name, email = email, address = address, mobile = number, gender = gender, status = status, 
                                   availableVacation = vacation, approvedVacation = 0, dob = dob, salary = salary)
           return redirect('hr-home')
      else:
           messages.ERROR(request, 'Error')
      
    else:
        form = UserCreationForm()
    return render(request, 'Users/addEmployees.html',{'form': form})

def update(request):
        return render(request, 'Users/update.html')