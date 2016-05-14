# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscription',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='suscriptions', serialize=False, to='clients.Client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='id',
            field=models.BigIntegerField(auto_created=True, verbose_name='ID'),
        ),
    ]
