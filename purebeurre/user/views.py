from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    return render(request, 'user/register.html')

def login(request):
    return render(request, 'user/login.html')

def profile(request):
    return render(request, 'user/profile.html')

def logout_view(request):
    return HttpResponse('<h1>Log-out</h1>')

