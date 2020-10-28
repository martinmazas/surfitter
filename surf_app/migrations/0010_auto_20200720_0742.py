# Generated by Django 3.0.6 on 2020-07-20 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surf_app', '0009_auto_20200720_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user',
        ),
        migrations.AddField(
            model_name='myuser',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_name',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='myuser',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='fullname',
            field=models.CharField(default='', max_length=30),
        ),
    ]