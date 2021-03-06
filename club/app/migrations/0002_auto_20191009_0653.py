# Generated by Django 2.2.6 on 2019-10-09 06:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumno',
            options={},
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='fecha_de_inscripcion',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='tipo_de_paquete',
        ),
        migrations.RemoveField(
            model_name='sesion',
            name='alumno',
        ),
        migrations.CreateModel(
            name='PaqueteAlumno',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='id del Paquete', primary_key=True, serialize=False)),
                ('fecha_de_inscripcion', models.DateField(blank=True, null=True)),
                ('tipo_de_paquete', models.CharField(choices=[('s', 'Por Hora'), ('m', '12 horas'), ('b', '20 horas')], help_text='Elige el tipo de paquete del alumno', max_length=1)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Alumno')),
                ('sesion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Sesion')),
            ],
            options={
                'ordering': ['fecha_de_inscripcion'],
            },
        ),
    ]
