# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('bill_date', models.DateField(default=datetime.datetime.now, verbose_name='\u8d26\u5355\u65e5\u671f')),
                ('amount', models.DecimalField(verbose_name='\u91d1\u989d', max_digits=10, decimal_places=2)),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0', blank=True)),
                ('user', models.ForeignKey(verbose_name='\u6d88\u8d39\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8bb0\u8d26',
                'verbose_name_plural': '\u8bb0\u8d26',
            },
            bases=(models.Model,),
        ),
    ]
