# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_auto_20180321_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='Last_name',
            new_name='last_name',
        ),
    ]