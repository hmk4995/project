# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0011_test_case'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test_case',
            old_name='question',
            new_name='qno',
        ),
    ]