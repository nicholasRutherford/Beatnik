# Generated by Django 2.2.9 on 2020-01-26 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beatnik', '0017_music_tidal_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FormSubmit',
        ),
        migrations.DeleteModel(
            name='MusicAccess',
        ),
    ]
