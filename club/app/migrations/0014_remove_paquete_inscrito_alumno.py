# Generated by Django 2.2.6 on 2019-10-11 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_paquete_inscrito_sesiones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquete_inscrito',
            name='alumno',
        ),
    ]
