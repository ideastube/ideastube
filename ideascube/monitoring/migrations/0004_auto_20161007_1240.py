# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0003_auto_20161007_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='name',
            field=models.CharField(max_length=300, verbose_name='name'),
        ),
    ]
