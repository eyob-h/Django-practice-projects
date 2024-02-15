from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    des = request.POST['description']
    # Tasks = Task.objects.all()
    # Tasks.save()
    Task.objects.create(title=task, description=des)
    return redirect('home')

def markAsCompleted(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.status == True:
        task.status = False
    else:
        task.status = True
    task.save()
    return redirect('home')

def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
# A single if else can do the trick
# def markAsUndone(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     task.status = False
#     task.save()
#     return redirect('home')