# Generated by Django 2.2.6 on 2020-01-03 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20200102_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='search_field',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
