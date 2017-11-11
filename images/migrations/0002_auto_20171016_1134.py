# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 11:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_created', to=settings.AUTH_USER_MODEL),
        ),
    ]