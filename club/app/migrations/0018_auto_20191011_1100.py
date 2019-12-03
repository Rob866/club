# Generated by Django 2.2.6 on 2019-10-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20191011_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete_inscrito',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Activo'), ('f', 'Finalizado')], help_text='Elige el estado del paquete', max_length=1),
        ),
    ]
