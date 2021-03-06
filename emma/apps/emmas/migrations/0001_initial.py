# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-24 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emma',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to=b'profile_pictures')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('main_occupation', models.TextField(blank=True, null=True, verbose_name='Main occupation')),
                ('general_description', models.TextField(blank=True, max_length=500, null=True, verbose_name='General Description')),
                ('qualities', models.TextField(blank=True, max_length=500, null=True, verbose_name='Qualities')),
                ('experience_with_seniors', models.TextField(blank=True, max_length=500, null=True, verbose_name='Experience with Seniors')),
                ('characteristics', models.TextField(blank=True, max_length=500, null=True, verbose_name='Characteristics')),
            ],
            options={
                'verbose_name': 'Emma',
                'verbose_name_plural': 'Emmas',
            },
        ),
        migrations.CreateModel(
            name='EmmaCertification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.CharField(max_length=100, verbose_name='Certification')),
                ('time', models.CharField(max_length=100, verbose_name='Time')),
                ('emma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emmas.Emma', verbose_name='Emma')),
            ],
            options={
                'verbose_name': 'Emma Certification',
                'verbose_name_plural': 'Emma Certifications',
            },
        ),
        migrations.CreateModel(
            name='EmmaCoordinator',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('profile_picture', models.ImageField(upload_to=b'profile_pictures')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone')),
            ],
        ),
        migrations.CreateModel(
            name='EmmaHobbie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbie', models.TextField(max_length=200, verbose_name='Hobbie')),
                ('emma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emmas.Emma', verbose_name='Emma')),
            ],
            options={
                'verbose_name': 'Emma Hobbie',
                'verbose_name_plural': 'Emma Hobbies',
            },
        ),
        migrations.CreateModel(
            name='EmmaStudies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studie', models.CharField(max_length=50, verbose_name='Studie')),
                ('emma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emmas.Emma', verbose_name='Emma')),
            ],
            options={
                'verbose_name': 'Emma Studie',
                'verbose_name_plural': 'Emma Studies',
            },
        ),
        migrations.CreateModel(
            name='PotentialEmma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('age', models.CharField(max_length=100, verbose_name='Age')),
                ('movile_phone', models.CharField(max_length=100, verbose_name='Movile phone')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone')),
                ('school_grade', models.CharField(max_length=100, verbose_name='School grade')),
                ('address', models.TextField(verbose_name='Address')),
                ('how_met_emma', models.CharField(max_length=100, verbose_name='How met Emma')),
                ('has_facebook', models.BooleanField(default=False, verbose_name='Has Facebook')),
                ('has_smathphone', models.BooleanField(default=False, verbose_name='Has smathphone')),
            ],
            options={
                'verbose_name': 'Potential Emma',
                'verbose_name_plural': 'Potential Emmas',
            },
        ),
    ]
