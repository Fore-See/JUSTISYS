# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('judg_num', models.AutoField(serialize=False, primary_key=True)),
                ('acc_date', models.DateField(null=True, blank=True)),
                ('p_assertion', models.CharField(max_length=45, null=True, blank=True)),
                ('d_assertion', models.CharField(max_length=45, null=True, blank=True)),
                ('location', models.CharField(max_length=45, null=True, blank=True)),
                ('judge', models.CharField(max_length=45, null=True, blank=True)),
                ('judg_date', models.DateField(null=True, blank=True)),
                ('judgefee', models.IntegerField(null=True, db_column=b'judgeFee', blank=True)),
                ('judgeid', models.CharField(max_length=45, db_column=b'judgeID')),
                ('judgereason', models.CharField(max_length=45, null=True, db_column=b'judgeReason', blank=True)),
                ('judgeresult', models.CharField(max_length=45, null=True, db_column=b'judgeResult', blank=True)),
                ('pfee', models.IntegerField(null=True, db_column=b'pFee', blank=True)),
                ('dfee', models.IntegerField(null=True, db_column=b'dFee', blank=True)),
                ('total_damage', models.IntegerField(null=True, db_column=b'Total_Damage', blank=True)),
                ('inverstigation', models.CharField(max_length=45, null=True, blank=True)),
                ('injured', models.CharField(max_length=45, null=True, blank=True)),
                ('highway', models.CharField(max_length=45, null=True, blank=True)),
                ('time', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'attribute',
            },
        ),
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
        migrations.DeleteModel(
            name='Judgement',
        ),
    ]
