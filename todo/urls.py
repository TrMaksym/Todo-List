from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/', views.tag_list, name='tag_list'),
    path('task/add/', views.task_add, name='task_add'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
    path('tag/add/', views.tag_add, name='tag_add'),
    path('tag/<int:pk>/update/', views.tag_update, name='tag_update'),
    path('tag/<int:pk>/delete/', views.tag_delete, name='tag_delete'),
]

app_name = "Todo"