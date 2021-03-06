# Generated by Django 2.2.6 on 2019-10-13 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20191011_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete_inscrito',
            name='alumno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clases_concluidas', to='app.Alumno'),
        ),
        migrations.AlterField(
            model_name='paquete_inscrito',
            name='status',
            field=models.BooleanField(blank=True, choices=[(True, 'Activo'), (False, 'Finalizado')], help_text='Elige el estado del paquete', max_length=1),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='observaciones',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
