# Generated by Django 2.2.6 on 2020-01-03 02:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_auto_20200102_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='search_field',
            field=models.CharField(default=models.UUIDField(default=uuid.uuid4, help_text='id del Alumno', primary_key=True, serialize=False), max_length=50),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='id del Alumno', primary_key=True, serialize=False),
        ),
    ]