# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 11:51
from __future__ import unicode_literals

import coding.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0013_auto_20160608_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_case',
            name='outputs',
            field=models.FileField(upload_to=coding.models.qstn_test_output_path),
        ),
    ]
