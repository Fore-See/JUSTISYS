# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20150803_1432'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CrashType',
        ),
        migrations.DeleteModel(
            name='Lawyer',
        ),
        migrations.DeleteModel(
            name='Situation',
        ),
        migrations.DeleteModel(
            name='Vechical',
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
    ]
