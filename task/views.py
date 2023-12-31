from django.shortcuts import render

def task_form(request):
    return render(request, 'task_form.html')
