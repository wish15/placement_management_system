# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='c_ad_details',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='register',
            name='c_details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='c_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
