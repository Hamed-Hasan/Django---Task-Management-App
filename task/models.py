from django.db import models

class TaskCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class TaskModel(models.Model):
    task_title = models.CharField(max_length=255)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField()
    categories = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.taskTitle
