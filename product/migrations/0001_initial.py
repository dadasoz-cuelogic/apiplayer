# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 08:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('creation_date_time', models.DateTimeField(auto_now_add=True)),
                ('modified_date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('creation_date_time', models.DateTimeField(auto_now_add=True)),
                ('modified_date_time', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catagory', to='product.Catagory')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
