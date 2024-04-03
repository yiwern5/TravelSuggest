from django.shortcuts import render

def home(request):
    data = { }
    return render(request, 'base/home.html', data)