# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_crashtype_lawyer_situation_vechical_weather'),
    ]

    operations = [
        migrations.CreateModel(
            name='Damageitem',
            fields=[
                ('number', models.AutoField(serialize=False, primary_key=True)),
                ('judgeid', models.CharField(max_length=45, null=True, db_column=b'judgeID', blank=True)),
                ('item', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'damageitem',
            },
        ),
    ]
