from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def index(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    tasks = Task.objects.all()
    context = {'tasks':tasks, 'form':form}
    return render(request, 'to_do_app/index.html', context)

def mark_as_done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.status = True if task.status==False else False
    task.save()
    return redirect('home')


def delete_task(request, task_id):
    task = Task.object.get(pk=task_id)
    task.delete()
    return redirect('home')

def edit_task(request, task_id):
    pass
def view_task(request, task_id):
    pass
