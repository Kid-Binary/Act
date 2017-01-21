# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-21 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата та час розсилки')),
            ],
            options={
                'verbose_name': 'Розсилка',
                'verbose_name_plural': 'Розсилки',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активний')),
                ('subscribed_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата та час підписки')),
                ('checkout_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата та час запиту')),
                ('checkout_hash', models.CharField(blank=True, default=None, max_length=40, null=True)),
            ],
            options={
                'verbose_name': 'Підписник',
                'verbose_name_plural': 'Підписники',
            },
        ),
        migrations.AddField(
            model_name='mailing',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='mailings', to='subscription.Subscriber'),
        ),
    ]
