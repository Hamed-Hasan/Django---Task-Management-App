from django import forms
from .models import TaskModel, TaskCategory

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_title', 'task_description', 'is_completed', 'task_assign_date', 'categories']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = ['category_name']
