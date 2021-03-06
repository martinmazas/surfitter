# Generated by Django 3.0.6 on 2020-07-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('surf_app', '0011_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('user_name', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=20)),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
    ]
