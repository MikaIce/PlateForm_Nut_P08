# Generated by Django 4.0.6 on 2022-07-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brands',
            field=models.CharField(default='', max_length=100, verbose_name='Marques du produit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='fat',
            field=models.FloatField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.URLField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='nutriscore',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='salt',
            field=models.FloatField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='saturated_fat',
            field=models.FloatField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sugars',
            field=models.FloatField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nom du produit'),
        ),
    ]
