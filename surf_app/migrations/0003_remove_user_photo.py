# Generated by Django 3.0.6 on 2020-07-19 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surf_app', '0002_auto_20200718_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
    ]