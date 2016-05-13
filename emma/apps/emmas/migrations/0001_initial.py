# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('movile_phone', models.PositiveIntegerField()),
                ('phone', models.PositiveIntegerField()),
                ('school_grade', models.CharField(max_length=15)),
                ('how_met_emma', models.CharField(max_length=15)),
                ('has_facebook', models.BooleanField(default=False)),
                ('has_smathphone', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Emma',
                'verbose_name_plural': 'Emmas',
            },
        ),
    ]
