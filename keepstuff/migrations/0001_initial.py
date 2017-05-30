# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=10)),
                ('quant', models.IntegerField(default=0)),
                ('catg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keepstuff.Category')),
            ],
        ),
    ]