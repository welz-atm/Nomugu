from django.contrib import admin
from .models import Market


class MarketAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Market, MarketAdmin)



