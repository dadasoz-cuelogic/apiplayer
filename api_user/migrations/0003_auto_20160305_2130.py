# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0002_auto_20160305_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_user',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Organization'), (3, 'Developer')], default=3),
        ),
    ]
