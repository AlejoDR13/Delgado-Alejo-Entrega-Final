# Generated by Django 3.2.16 on 2022-11-29 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0011_auto_20221129_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peliculas',
            name='id',
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='titulo',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
