from django.db import models
from django.utils import timezone


class Employee(models.Model):
    id = models.IntegerField(primary_key = True, unique = True, error_messages = {'null': 'ID field cannot be null','unique': 'This ID is already in use'})
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    address = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 11)
    gender = models.CharField(max_length = 6)
    availableVacation = models.IntegerField()
    approvedVacation = models.IntegerField()
    salary = models.IntegerField()
    dob = models.DateTimeField()
    dateCreated = models.DateTimeField(default= timezone.now)
