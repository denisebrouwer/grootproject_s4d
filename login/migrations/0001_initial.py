# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-28 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
            ],
        ),
    ]
