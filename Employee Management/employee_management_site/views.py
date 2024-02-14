from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee
# from django.http import *

def home(request):
    # return HttpResponse("hi home")
    employees = Employee.objects.all()

    context = {
        'employees' : employees,
    }
    return render(request, 'home.html', context)