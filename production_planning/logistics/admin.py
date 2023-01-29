from django.contrib import admin


from logistics.models import Logistics


@admin.register(Logistics)
class LogisticsAdmin(admin.ModelAdmin):
    list_display = ('n_po','dispatch_date','client','address','dispatch',)
    list_filter = ('dispatch_date',)
    search_fields = ('n_po',)


