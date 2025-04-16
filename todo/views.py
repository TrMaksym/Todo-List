from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task, Tag
from .forms import TaskForm, TagForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

class TagListView(ListView):
    model = Tag
    template_name = 'todo/tag_list.html'
    context_object_name = 'tags'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('Todo:index')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('Todo:index')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('Todo:index')

class TaskToggleView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('Todo:index')

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('Todo:tag_list')

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('Todo:tag_list')

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'todo/tag_confirm_delete.html'
    success_url = reverse_lazy('Todo:tag_list')