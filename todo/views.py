from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .forms import TaskForm, TagForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'todo/tag_list.html', {'tags': tags})

def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Todo:index')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('Todo:index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('Todo:index')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('Todo:index')

def tag_add(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Todo:tag_list')
    else:
        form = TagForm()
    return render(request, 'todo/tag_form.html', {'form': form})

def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('Todo:tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'todo/tag_form.html', {'form': form})

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('Todo:tag_list')
    return render(request, 'todo/tag_confirm_delete.html', {'tag': tag})