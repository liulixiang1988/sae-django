#-*- coding:utf-8 -*-

import datetime

from django.db import models

from django.contrib.auth.models import User


class BillType(models.Model):
    bill_type = models.CharField(u'类型', max_length=20)

    class Meta:
        verbose_name = u'账单类型'
        verbose_name_plural = u'账单类型'

    def __unicode__(self):
        return self.bill_type


class Bill(models.Model):
    user = models.ForeignKey(User, verbose_name=u'消费者')
    bill_type = models.ForeignKey(BillType, verbose_name=u'类型', null=True, blank=True)
    create_date = models.DateTimeField(u'创建日期', auto_now_add=True)
    bill_date = models.DateField(u'账单日期', default=datetime.datetime.now)
    amount = models.DecimalField(u'金额', max_digits=10, decimal_places=2)
    description = models.TextField(u'描述', blank=True)

    class Meta:
        verbose_name = u'记账'
        verbose_name_plural = u'记账'

