# Generated by Django 2.2.6 on 2019-12-20 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20191220_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
