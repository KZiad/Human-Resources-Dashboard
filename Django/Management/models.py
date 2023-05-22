from django.db import models
import datetime


class Employee(models.Model):
    id = models.IntegerField(primary_key = True, unique = True, error_messages = {'null': 'ID field cannot be null','unique': 'This ID is already in use'})
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    address = models.CharField(max_length = 100)
    number = models.CharField(max_length = 11)
    gender = models.CharField(max_length = 6)
    status = models.CharField(max_length= 12)
    availableVacation = models.IntegerField()
    approvedVacation = models.IntegerField(default= 0)
    salary = models.IntegerField()
    dob = models.DateField()
    dateCreated = models.DateField(default= datetime.date.today, null= True)

    # This is to be able to read the employee name and ID in admin menu
    def __str__(self):
        return f'{self.name} -- {self.id}'
