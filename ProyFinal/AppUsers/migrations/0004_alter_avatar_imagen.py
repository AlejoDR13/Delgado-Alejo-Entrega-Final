# Generated by Django 3.2.16 on 2022-11-29 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsers', '0003_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
