# Generated by Django 3.2.16 on 2022-12-11 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0022_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
    ]
