from django.contrib import admin
from .models import TaskModel, TaskCategory

admin.site.register(TaskModel)
admin.site.register(TaskCategory)
