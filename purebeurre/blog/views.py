from django.http import HttpResponse
from django.shortcuts import render

def paginate(request):
    return HttpResponse('<h1> paginate </h1>')

def search(request):
    return render(request, 'blog/search.html')

def product(request):
    return render(request, 'blog/product.html')

def substitute(request):
    return render(request, 'blog/substitute.html')

def save(request):
    return HttpResponse('<h1>save</h1>')

def favorite(request):
    return render(request, 'blog/favorite.html')

def delete(request):
    return HttpResponse('<h1>supprime</h1>')