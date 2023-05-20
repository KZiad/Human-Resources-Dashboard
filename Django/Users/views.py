from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def createEmployee(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
           name = form.cleaned_data.get('name')
           messages.success(request, 'Employee created successfully')
           return redirect('hr-home')
      else:
           messages.ERROR(request, 'Error')
      
    else:
        form = UserCreationForm()
    return render(request, 'Users/addEmployees.html',{'form': form})

def update(request):
        return render(request, 'Users/update.html')