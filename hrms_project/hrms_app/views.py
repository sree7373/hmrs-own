#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})