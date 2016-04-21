# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0007_auto_20160421_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user_id',
            field=models.IntegerField(default=1, unique=True),
        ),
        migrations.AlterField(
            model_name='contest',
            name='college_name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='contest',
            name='contest_name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='contest',
            name='questions',
            field=models.CommaSeparatedIntegerField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='input_format',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='output_format',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='sample',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='submission',
            name='language',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='submission',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='coding.Question'),
        ),
        migrations.AlterField(
            model_name='user',
            name='admin_privilege',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
