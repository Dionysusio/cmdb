# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0002_auto_20170810_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='in_use',
            field=models.CharField(max_length=32, null=True, verbose_name='进流量'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='out_use',
            field=models.CharField(max_length=32, null=True, verbose_name='出流量'),
        ),
    ]