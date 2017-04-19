# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 12:14
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170419_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Topics'),
        ),
    ]
