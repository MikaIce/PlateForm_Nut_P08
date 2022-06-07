from django.urls import path
from .views import index, article, base, nav, search, register, login, legal

urlpatterns = [
    path('', index, name="index"),
    path('article<str:numero_article>/', article, name="blog-article"),
    path('base/', base, name="base-html"),
    path('nav', nav, name="nav-html"),
    path('search', search, name="search-html"),
    path('register', register, name="register-html"),
    path('login', login, name="login-html"),
    path('legal', legal, name="legal-html"),
]