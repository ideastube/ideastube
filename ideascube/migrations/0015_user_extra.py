# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideascube', '0014_user_disabilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='extra',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]