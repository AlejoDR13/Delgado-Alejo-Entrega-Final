# Generated by Django 3.2.16 on 2022-11-29 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsers', '0002_userabout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(null=True, upload_to='avatares'),
        ),
    ]