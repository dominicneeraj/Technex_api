# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Token', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='fro',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='word',
            name='to',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='word',
            name='code',
            field=models.TextField(default=b''),
        ),
    ]
