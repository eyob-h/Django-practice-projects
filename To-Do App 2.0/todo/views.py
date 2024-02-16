from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
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

# A single if else can do the trick
# def markAsUndone(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     task.status = False
#     task.save()
#     return redirect('home')


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

#EDIT TASK
def editTask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)

    # we can also avoid making the updateTask endpoint by making a conditional statement
    # if request.method == 'POST':
    #     request.POST['task'] = get_task.title
    #     request.POST['description'] = get_task.description
    #     return redirect('home')
    # else:
    #     context = {
    #         'get_task':get_task
    #     } 
    #     return render(request, 'edit.task.html',context)


#Update Task

def updateTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.title = request.POST['task']
    task.description = request.POST['description']
    task.save()

    # return HttpResponse("UPDATED STUFF MY GUY", task.title, task.description)
    return redirect('home')


