# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20150805_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullContent',
            fields=[
                ('judg_num', models.IntegerField(serialize=False, primary_key=True)),
                ('judgeid', models.CharField(max_length=45, null=True, db_column=b'JudgeID', blank=True)),
                ('content', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'full_content',
            },
        ),
        migrations.AddField(
            model_name='attribute',
            name='dlawyer',
            field=models.IntegerField(null=True, db_column=b'dLawyer', blank=True),
        ),
        migrations.AddField(
            model_name='attribute',
            name='duration',
            field=models.IntegerField(null=True, db_column=b'Duration', blank=True),
        ),
        migrations.AddField(
            model_name='attribute',
            name='plawyer',
            field=models.IntegerField(null=True, db_column=b'pLawyer', blank=True),
        ),
        migrations.AddField(
            model_name='attribute',
            name='win_lose',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
