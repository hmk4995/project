# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0008_auto_20160421_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='no_of_test_cases',
            field=models.IntegerField(default=0),
        ),
    ]