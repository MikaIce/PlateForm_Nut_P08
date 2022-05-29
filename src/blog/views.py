from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")

def article(request, numero_article):
    if numero_article in ["1", "2", "3"]:
        return render(request, f"blog/article{numero_article}.html")
    return render(request, "blog/article_not_found.html")

def base(request):
    return render(request, "blog/base.html")