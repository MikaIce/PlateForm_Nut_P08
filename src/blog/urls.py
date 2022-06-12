from django.urls import path
from .views import index, nav, search, register, login, legal, base

urlpatterns = [
    path('', index, name="index"),
    path('nav', nav, name="nav-html"),
    path('search', search, name="search-html"),
    path('register', register, name="register-html"),
    path('login', login, name="login-html"),
    path('legal', legal, name="legal-html"),
    path('base', base, name="base"),
]