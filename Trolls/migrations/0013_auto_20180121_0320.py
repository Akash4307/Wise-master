# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trolls', '0012_auto_20180121_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='UserLocation',
            field=models.CharField(max_length=500),
        ),
    ]