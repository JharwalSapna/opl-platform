# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-07 06:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathers_name', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('cellphone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('chat_id', models.CharField(blank=True, max_length=150, verbose_name='Chat ID')),
                ('full_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
