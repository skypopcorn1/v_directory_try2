# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-29 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20170629_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='mantra',
            field=models.CharField(default='Total Champion', max_length=25),
            preserve_default=False,
        ),
    ]
