# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-03 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adults', '0011_adult_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdultHobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbie', models.CharField(max_length=50, verbose_name='Hobbie')),
                ('adult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adults.Adult', verbose_name='Adult')),
            ],
            options={
                'verbose_name': 'Adult Hobbie',
                'verbose_name_plural': 'Adult Hobbie',
            },
        ),
    ]