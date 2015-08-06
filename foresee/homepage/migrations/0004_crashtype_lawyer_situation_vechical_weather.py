# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20150803_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrashType',
            fields=[
                ('number', models.AutoField(serialize=False, primary_key=True)),
                ('judgeid', models.CharField(max_length=45, null=True, db_column=b'judgeID', blank=True)),
                ('crash_type', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'crash_type',
            },
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('number', models.AutoField(serialize=False, primary_key=True)),
                ('judgeid', models.CharField(max_length=45, null=True, db_column=b'judgeID', blank=True)),
                ('pord', models.CharField(max_length=45, null=True, db_column=b'PorD', blank=True)),
                ('lawyer', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'lawyer',
            },
        ),
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('number', models.AutoField(serialize=False, primary_key=True)),
                ('judgeid', models.CharField(max_length=45, null=True, db_column=b'judgeID', blank=True)),
                ('judgesituation', models.CharField(max_length=45, null=True, db_column=b'judgeSituation', blank=True)),
            ],
            options={
                'db_table': 'situation',
            },
        ),
        migrations.CreateModel(
            name='Vechical',
            fields=[
                ('number', models.AutoField(serialize=False, primary_key=True)),
                ('judgeid', models.CharField(max_length=45, null=True, db_column=b'judgeID', blank=True)),
                ('pord', models.CharField(max_length=45, null=True, db_column=b'PorD', blank=True)),
                ('cartype', models.CharField(max_length=45, null=True, db_column=b'carType', blank=True)),
            ],
            options={
                'db_table': 'vechical',
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('number', models.AutoField(serialize=False, primary_key=True)),
                ('judgeid', models.CharField(max_length=45, null=True, db_column=b'judgeID', blank=True)),
                ('weather', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'weather',
            },
        ),
    ]
