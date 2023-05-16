from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Emp_Id=models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee, related_name='departments')

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()   
