# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('cost', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bills',
            name='shared_with',
        ),
        migrations.DeleteModel(
            name='Bills',
        ),
        migrations.AddField(
            model_name='bill',
            name='items',
            field=models.ForeignKey(to='billing.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='shared_with',
            field=models.ManyToManyField(to='accounts.UserProfile', blank=True),
            preserve_default=True,
        ),
    ]
