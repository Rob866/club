# Generated by Django 2.2.6 on 2020-01-03 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_alumno_busqueda_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='busqueda_id',
            field=models.TextField(default='<djan'),
        ),
    ]
