from django import forms
from Management.models import Employee, Vacation


gender = (("Male", "Male"), ("Female", "Female"))
status = (("Single", "Single"), ("Married", "Married"), ("Widowed", "Widowed"))

class EmployeeRegistrationForm(forms.ModelForm):

    name = forms.CharField(label = 'name',max_length = 100, error_messages = {"required": "Please enter a name"}, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    id = forms.IntegerField(label= 'id', error_messages = {"required": "Please enter an ID"}, widget=forms.TextInput(attrs={'placeholder': 'ID'}))
    email = forms.EmailField(label= 'email', max_length = 254, error_messages = {"required": "Please enter an email"}, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    address = forms.CharField(label= 'address', max_length = 100, error_messages = {"required": "Please enter an address"}, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    number = forms.CharField(label= 'number', max_length = 11, error_messages = {"required": "Please enter a phone number"}, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    gender = forms.ChoiceField(choices= gender, error_messages = {"required": "Please specify your gender"})
    dob = forms.DateField(label= 'dob' ,error_messages = {"required": "Please enter your date of birth"}, widget = forms.NumberInput(attrs={'type':'date'}))
    status = forms.ChoiceField(choices= status, error_messages = {"required": "Please specify your status"})
    availableVacation = forms.IntegerField(label= 'availableVacation', error_messages = {"required": "Please enter the available vacation days"}, widget=forms.TextInput(attrs={'placeholder': 'Available Vacation Days'}))
    salary = forms.IntegerField(label= 'salary', error_messages = {"required": "Please enter the salary"}, widget=forms.TextInput(attrs={'placeholder': 'Salary'}))

    class Meta:
        model = Employee
        fields = ['name', 'id', 'email', 'address', 'number', 'gender', 'dob', 'status', 'availableVacation', 'salary']


class EmployeeUpdateForm(forms.ModelForm):

    name = forms.CharField(label = 'name',max_length = 100, error_messages = {"required": "Please enter a name"}, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    id = forms.IntegerField(label= 'id', disabled= True)
    email = forms.EmailField(label= 'email', max_length = 254, error_messages = {"required": "Please enter an email"}, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    address = forms.CharField(label= 'address', max_length = 100, error_messages = {"required": "Please enter an address"}, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    number = forms.CharField(label= 'number', max_length = 11, error_messages = {"required": "Please enter a phone number"}, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    gender = forms.ChoiceField(choices= gender, error_messages = {"required": "Please specify your gender"})
    dob = forms.DateField(label= 'dob' ,error_messages = {"required": "Please enter your date of birth"}, widget=forms.TextInput(attrs={'placeholder': ' Year-Month-Day'}))
    status = forms.ChoiceField(choices= status, error_messages = {"required": "Please specify your status"})
    availableVacation = forms.IntegerField(label= 'availableVacation', error_messages = {"required": "Please enter the available vacation days"}, widget=forms.TextInput(attrs={'placeholder': 'Available Vacation Days'}))
    approvedVacation = forms.IntegerField(label= 'availableVacation',disabled= True, initial= 0)
    salary = forms.IntegerField(label= 'salary', error_messages = {"required": "Please enter the salary"}, widget=forms.TextInput(attrs={'placeholder': 'Salary'}))

    class Meta:
        model = Employee
        fields = ['name', 'id', 'email', 'address', 'number', 'gender', 'dob', 'status', 'availableVacation', 'salary']


class EmployeeVacationForm(forms.ModelForm):
    # Auto filled fields
    employeeID = forms.IntegerField(label= 'id', disabled= True)
    EmployeeName = forms.CharField(label = 'name',max_length = 100, disabled= True)
    
    # User input fields
    beginDate = forms.DateField(label= 'beginDate' ,error_messages = {"required": "Please enter the begin date"}, widget=forms.TextInput(attrs={'placeholder': ' Year-Month-Day'}))
    endDate = forms.DateField(label= 'endDate' ,error_messages = {"required": "Please enter the end date"}, widget=forms.TextInput(attrs={'placeholder': ' Year-Month-Day'}))
    reason = forms.CharField(label= 'reason', max_length = 1000, error_messages = {"required": "Please enter the reason"}, widget=forms.TextInput(attrs={'placeholder': 'Reason'}))
    
    class Meta:
        model = Vacation
        fields = ['employeeID', 'beginDate', 'endDate', 'status', 'reason']