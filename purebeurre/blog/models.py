from django.db import models

class Product(models.Model):
    name = models.fields.CharField(max_length=100)

class Category(models.Model):
    name = models.fields.CharField(max_length=100)

class Favorite(models.Model):
    name = models.fields.CharField(max_length=100)