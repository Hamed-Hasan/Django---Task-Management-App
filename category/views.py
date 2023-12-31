from django.shortcuts import render

def category_form(request):
    return render(request, 'category_form.html')
