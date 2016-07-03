# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_client_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_service', models.IntegerField(blank=True, null=True, verbose_name='ID Service')),
                ('workshop_list', models.CharField(blank=True, max_length=50, null=True, verbose_name='Workshop List')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client', verbose_name='Client')),
            ],
        ),
    ]