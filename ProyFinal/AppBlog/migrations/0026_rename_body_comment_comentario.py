# Generated by Django 3.2.16 on 2022-12-11 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0025_auto_20221211_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comentario',
        ),
    ]