# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trolls', '0005_auto_20171220_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='Link',
            new_name='UserLink',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='Location',
            new_name='UserLocation',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='Name',
            new_name='UserName',
        ),
    ]