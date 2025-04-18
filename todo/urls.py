from django.urls import path
from . import views

app_name = 'Todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('task/add/', views.TaskCreateView.as_view(), name='task_add'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/toggle/', views.TaskToggleView.as_view(), name='task_toggle'),
    path('tag/add/', views.TagCreateView.as_view(), name='tag_add'),
    path('tag/<int:pk>/update/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
]
