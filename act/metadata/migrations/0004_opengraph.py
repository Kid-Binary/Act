# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-20 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import metadata.models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0003_auto_20170120_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='open_graph', to='metadata.Metadata')),
            ],
            bases=(metadata.models.MetadataAttributeMixin, models.Model),
        ),
    ]