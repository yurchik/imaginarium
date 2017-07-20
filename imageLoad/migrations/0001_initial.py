# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='uploads/')),
                ('desc', models.CharField(default='Описание картинки не задано', max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('rate', models.IntegerField(default=0)),
            ],
        ),
    ]
