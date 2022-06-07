from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")

def article(request, numero_article):
    if numero_article in ["1", "2", "3"]:
        return render(request, f"blog/article{numero_article}.html")
    return render(request, "blog/register.html")

def base(request):
    return render(request, "blog/index.html")

def nav(request):
    return render(request, "blog/nav.html")

def search(request):
    return render(request, "blog/search.html")

def register(request):
    return render(request, "blog/register.html")

def login(request):
    return render(request, "blog/login.html")

def legal(request):
    return render(request, "blog/legal.html")
