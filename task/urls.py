from django.urls import path
from .views import show_tasks, add_task, edit_task, delete_task, add_category

urlpatterns = [
    path('show/', show_tasks, name='show_tasks'),
    path('add/', add_task, name='add_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('add_category/', add_category, name='add_category'),
]
