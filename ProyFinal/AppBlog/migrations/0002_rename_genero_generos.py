# Generated by Django 3.2.16 on 2022-11-28 16:13

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    initial = True

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genero',
            new_name='Generos',
        ),
    ]
