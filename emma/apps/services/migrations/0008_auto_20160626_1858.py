# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20160620_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedays',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
