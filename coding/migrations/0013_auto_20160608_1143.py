# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 11:43
from __future__ import unicode_literals

import coding.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0012_auto_20160608_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_case',
            name='inputs',
            field=models.FileField(upload_to=coding.models.qstn_test_input_path),
        ),
    ]
