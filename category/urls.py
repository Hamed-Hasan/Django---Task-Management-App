from django.urls import path
from .views import category_form

urlpatterns = [
    path('form/', category_form, name='category_form'),
    # Add more URL patterns as needed
]
