# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-14 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20170114_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-created_at', '-id'), 'verbose_name': 'Подія', 'verbose_name_plural': '  Події'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-started_at', '-id'), 'verbose_name': 'Проект', 'verbose_name_plural': '    Проекти'},
        ),
    ]
