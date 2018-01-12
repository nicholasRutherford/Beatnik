# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatnik', '0007_auto_20171224_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='apple_url',
            field=models.URLField(null=True, unique=True, verbose_name='Apple Music URL'),
        ),
        migrations.AlterField(
            model_name='music',
            name='gpm_url',
            field=models.URLField(null=True, unique=True, verbose_name='Google Play Music URL'),
        ),
        migrations.AlterField(
            model_name='music',
            name='soundcloud_url',
            field=models.URLField(null=True, unique=True, verbose_name='Soundcloud URL'),
        ),
        migrations.AlterField(
            model_name='music',
            name='spotify_url',
            field=models.URLField(null=True, unique=True, verbose_name='Spotify URL'),
        ),
    ]
