# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160305_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_key',
            field=models.CharField(db_index=True, max_length=32, null=True, unique=True),
        ),
    ]