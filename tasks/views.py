from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.shortcuts import get_object_or_404


def task_list(request):
    if not request.user.is_authenticated:
        return render(request, 'tasks/task_list.html', {'tasks': []})
    
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
        
    else:
        form = TaskForm()
    return render(request,'tasks/create_task.html', {'form': form})


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'completed'
    task.save()
    return redirect('task_list')

def task_description(request,task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'tasks/task_description.html',{'task': task})

def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')