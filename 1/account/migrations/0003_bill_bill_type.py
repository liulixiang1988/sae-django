# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_billtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='bill_type',
            field=models.ForeignKey(verbose_name='\u7c7b\u578b', blank=True, to='account.BillType', null=True),
            preserve_default=True,
        ),
    ]
