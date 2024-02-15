from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks =  Task.objects.filter(status = False).order_by('-updated_at')
    comp = Task.objects.filter(status=True).order_by('-updated_at')
    context = {
        'tasks' : tasks,
        'completed': comp
    }
    return render(request, 'home.html', context)