# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-28 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='users',
        ),
        migrations.AddField(
            model_name='quote',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_quotes', to='belt_app.User'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
