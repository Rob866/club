# Generated by Django 2.2.6 on 2019-12-28 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_mensaje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='body',
            new_name='mensaje',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='email',
        ),
    ]
