from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('paginate/', views.paginate),
    path('search/', views.search, name='search'),
    path('product/', views.product),
    path('substitute/', views.substitute),
    path('save/', views.save),
    path('favorite/', views.favorite, name='favorite'),
    path('delete/', views.delete),
]