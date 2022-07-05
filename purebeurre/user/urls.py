from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [

    path('register/', views.register),
    path('login/', views.login),
    path('profile/', views.profile),
    path('logout_view/', views.logout_view),

]