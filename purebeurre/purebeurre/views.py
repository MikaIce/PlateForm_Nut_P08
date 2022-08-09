from django.shortcuts import render

def index(request):
    return render(request, 'purebeurre/index.html')

def legal(request):
    return render(request, 'purebeurre/legal.html')

def my_404_view(request, exception):
    return render(request, 'purebeurre/404.html')

def my_500_view(request):
    return render(request, 'purebeurre/500.html')

