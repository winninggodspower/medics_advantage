# Generated by Django 5.1.5 on 2025-06-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_lectures', '0003_alter_videolecture_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videolecture',
            name='video',
            field=models.URLField(help_text='YouTube video URL', max_length=255),
        ),
    ]
