# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170514_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='username',
        ),
    ]
