from django.urls import path
from .views import task_form

urlpatterns = [
    path('', task_form, name='task_form'),
    # Add more URL patterns as needed
]
