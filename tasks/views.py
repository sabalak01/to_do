from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


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

