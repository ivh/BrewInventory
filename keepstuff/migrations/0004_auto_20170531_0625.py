# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 06:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keepstuff', '0003_auto_20170530_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='stuff',
            options={'ordering': ['catg', '-quant']},
        ),
    ]
