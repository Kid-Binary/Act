# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-05 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20170205_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='modified_at',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата оновлення'),
        ),
    ]