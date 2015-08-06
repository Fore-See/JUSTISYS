# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_damageitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='crashtype',
            name='judg_num',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='damageitem',
            name='judg_num',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='judg_num',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='situation',
            name='judg_num',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='vechical',
            name='judg_num',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='judg_num',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
