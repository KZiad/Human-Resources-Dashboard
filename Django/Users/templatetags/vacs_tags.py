from django import template
from Management.models import Employee
register = template.Library()


@register.simple_tag
def get_vac_emp_name(*args, **kwargs):
    empID = args[0].employeeID
    # Get the employee's name from the employee ID through the model
    employee = Employee.objects.get(id = empID)[0]
    return employee.name

@register.simple_tag
def calc_vac_days(*args, **kwargs):
    startDate = args[0].startDate
    endDate = args[0].endDate
    numDaysDelta = endDate - startDate
    numDays = numDaysDelta.days
    return numDays
