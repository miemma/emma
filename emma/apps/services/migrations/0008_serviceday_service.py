# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-26 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20160926_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceday',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.HiredService'),
            preserve_default=False,
        ),
    ]
