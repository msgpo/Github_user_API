# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_user_info_search_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]
