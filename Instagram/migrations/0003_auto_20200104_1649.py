# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-04 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0002_auto_20200103_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
