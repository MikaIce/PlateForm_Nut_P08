from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")

def article(request, numero_article):
    if numero_article in ["1", "2", "3"]:
        return render(request, f"blog/article{numero_article}.html")
    return render(request, "blog/register.html")

def nav(request):
    return render(request, "blog/nav.html")

def search(request):
    """ Display product or products matching the user's request """
    query = request.GET.get('query')
    if query:
        # search by product name
        products = Product.objects.filter(
            name__icontains=query).order_by('nutriscore', 'id')

        # if nothing is found, search by brands name
        if not products.exists():
            products = Product.objects.filter(
                brands__icontains=query).order_by('nutriscore', 'id')
        # if nothing is found
        if not products.exists():
            messages.success(request,
                             "Nous n'avons trouvé aucun produit "
                             "correspondant à votre recherche")
            return redirect('index')

        context = {'page_obj': paginate(request, products, 9),
                   'query': query}
        return render(request, 'search.html', context)

    else:
        messages.success(request, "Vous n'avez rien saisi")
        return redirect('index')

def register(request):
    return render(request, "blog/register.html")

def login(request):
    return render(request, "blog/login.html")

def legal(request):
    return render(request, "blog/legal.html")

def base(request):
    return render(request, "blog/base.html")