# Generated by Django 2.2.6 on 2020-01-03 02:08

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_alumno_serach_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='serach_field',
            field=models.CharField(default=django.db.models.fields.Field.get_attname, max_length=100),
        ),
    ]