# Generated by Django 2.2.6 on 2020-01-03 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_remove_alumno_busqueda_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='busqueda_id',
            field=models.CharField(default='<djan', max_length=100),
        ),
    ]
