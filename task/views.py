from django.shortcuts import render, redirect
from .models import TaskModel, TaskCategory
from .forms import TaskForm, CategoryForm

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('show_tasks')
    return render(request, 'delete_task.html', {'task': task})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('show_tasks')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})