# Generated by Django 2.2.6 on 2019-12-22 23:28

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191221_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
