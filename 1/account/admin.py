from django.contrib import admin

# Register your models here.

from .models import Bill, BillType


class BillAdmin(admin.ModelAdmin):
    list_display = ('user', 'bill_date', 'bill_type', 'amount')
    search_fields = ['user']

admin.site.register(Bill, BillAdmin)

admin.site.register(BillType)

