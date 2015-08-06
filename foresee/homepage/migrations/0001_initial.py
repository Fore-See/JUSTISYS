# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judgement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('court', models.TextField(null=True, db_column=b'Court', blank=True)),
                ('accidentdate', models.TextField(null=True, db_column=b'AccidentDate', blank=True)),
                ('judgedate', models.TextField(null=True, db_column=b'JudgeDate', blank=True)),
                ('assertionexisting', models.TextField(null=True, db_column=b'AssertionExisting', blank=True)),
                ('judge', models.TextField(null=True, db_column=b'Judge', blank=True)),
                ('judgefee', models.FloatField(null=True, db_column=b'JudgeFee', blank=True)),
                ('judgereason', models.TextField(null=True, db_column=b'JudgeReason', blank=True)),
                ('judgeid', models.TextField(null=True, db_column=b'JudgeId', blank=True)),
                ('totaldamage', models.FloatField(null=True, db_column=b'TotalDamage', blank=True)),
                ('pfee_dfee', models.TextField(null=True, db_column=b'PFee_DFee', blank=True)),
            ],
            options={
                'db_table': 'judgement',
            },
        ),
    ]
