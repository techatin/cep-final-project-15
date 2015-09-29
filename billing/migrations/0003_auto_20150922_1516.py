# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20150916_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='bill',
            field=models.ForeignKey(blank=True, to='billing.Bill', null=True),
        ),
    ]
