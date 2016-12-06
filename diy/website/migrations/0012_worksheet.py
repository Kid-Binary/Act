# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20161201_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300, verbose_name='ПІБ')),
                ('residence', models.CharField(max_length=500, verbose_name='Місце проживання')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=19, verbose_name='Телефон')),
                ('personal_link', models.URLField(blank=True, null=True, verbose_name='Персональна сторінка')),
                ('problem', models.BooleanField(verbose_name='Бажаєте повідомити про проблему?')),
                ('problem_description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Із якою проблемою Вам довелося зіштовхнутися?')),
                ('activity', models.BooleanField(verbose_name='Чи бажаєте Ви долучитись до «ДІЙ!»?')),
                ('activity_description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Із якою проблемою Вам довелося зіштовхнутися?')),
            ],
            options={
                'db_table': 'website_worksheet',
                'verbose_name_plural': '      Анкети',
                'verbose_name': 'Анкета',
            },
        ),
    ]
