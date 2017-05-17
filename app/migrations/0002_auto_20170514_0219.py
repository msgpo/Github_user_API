# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='email',
        ),
        migrations.AddField(
            model_name='user_info',
            name='followers',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_info',
            name='following',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_info',
            name='public_gists',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_info',
            name='public_repos',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_info',
            name='user_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_info',
            name='date_searched',
            field=models.DateField(),
        ),
    ]