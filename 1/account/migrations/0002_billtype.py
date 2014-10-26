# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_type', models.CharField(max_length=20, verbose_name='\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u8d26\u5355\u7c7b\u578b',
                'verbose_name_plural': '\u8d26\u5355\u7c7b\u578b',
            },
            bases=(models.Model,),
        ),
    ]
