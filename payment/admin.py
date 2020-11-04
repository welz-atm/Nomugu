from django.contrib import admin
from .models import Payment, Account


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'reference', 'amount', 'card_type', 'channel', 'bank_name')
    list_filter = ('user', 'payment_date', 'card_type', 'bank_name')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'bank_name', 'user',)
    list_filter = ('bank_name',)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Account, AccountAdmin)



