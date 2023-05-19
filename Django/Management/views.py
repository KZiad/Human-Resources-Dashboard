from django.shortcuts import render

empData = [
        {
                'name': 'Mohamed Waleed',
                'id': '20210363',
                'email': 'mohamed2003elashmawy@gmail.com',
                'address': '6 Abu Baker',
                'num': '01064207150',
                'gender': 'Male',
                'status': 'Single',
                'fVacation': '30',
                'aVacation': '9',
                'salary': '20000',
                'dob': '23-3-2003'
        }
]

def projects(request):
        return render(request, 'Management/projects.html')

def home(request):
        return render(request, 'Management/index.html')

def about(request):
        return render(request, 'Management/aboutUs.html')

def data(request):
        context = {
                'empData': empData
        }
        return render(request, 'Management/employeeData.html', context)

def newEmp(request):
        return render(request, 'Management/addEmployees.html')

def update(request):
        return render(request, 'Management/update.html')

def vacation(request):
        return render(request, 'Management/vacation.html')

def vacationList(request):
        return render(request, 'Management/vacationList.html')
