# Generated by Django 3.2.16 on 2022-11-29 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_rename_genero_generos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peliculas',
            name='genero',
        ),
    ]
