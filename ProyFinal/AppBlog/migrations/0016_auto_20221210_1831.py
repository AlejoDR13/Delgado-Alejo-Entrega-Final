# Generated by Django 3.2.16 on 2022-12-10 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0015_auto_20221208_1916'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RenameField(
            model_name='peliculas',
            old_name='autor_post',
            new_name='autor',
        ),
    ]
