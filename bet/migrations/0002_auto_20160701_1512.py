# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 15:12
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', ckeditor.fields.RichTextField()),
                ('weight', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=10)),
                ('titleOn', models.BooleanField(default=True)),
                ('sidebar', models.CharField(choices=[('left', 'Left'), ('right', 'Right')], default='right', max_length=10)),
            ],
            options={
                'ordering': ('-weight',),
            },
        ),
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
