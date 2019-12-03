# Generated by Django 2.2.6 on 2019-10-09 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_de_inscripcion', models.DateField(blank=True, null=True)),
                ('nivel_academico', models.CharField(blank=True, choices=[('k', 'Kinder'), ('p', 'Primaria'), ('s', 'Secundaria'), ('b', 'bachillerato'), ('u', 'universidad')], help_text='Elige el nivel académico del alumno', max_length=1)),
                ('tipo_de_paquete', models.CharField(choices=[('s', 'Por Hora'), ('m', '12 horas'), ('b', '20 horas')], help_text='Elige el tipo de paquete del alumno', max_length=1)),
            ],
            options={
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.CharField(max_length=100)),
                ('fecha_de_clase', models.DateField(blank=True, null=True)),
                ('hora_de_inicio', models.TimeField()),
                ('hora_de_salida', models.TimeField()),
                ('total_horas', models.IntegerField()),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Alumno')),
            ],
            options={
                'ordering': ['-fecha_de_clase'],
            },
        ),
    ]
