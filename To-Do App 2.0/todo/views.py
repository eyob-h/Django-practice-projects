from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    des = request.POST['description']
    # Tasks = Task.objects.all()
    # Tasks.save()
    Task.objects.create(title=task, description=des)
    return redirect('home')

