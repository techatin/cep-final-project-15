# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20150922_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bill',
            field=models.ForeignKey(related_name='items', blank=True, to='billing.Bill', null=True),
        ),
    ]
