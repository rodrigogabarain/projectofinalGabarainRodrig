from django.contrib import admin


from operative.models import Operative


@admin.register(Operative)
class OperativeAdmin(admin.ModelAdmin):
    list_display = ('n_po','production_entry_date','manufacturing_date','mp_mm','pt_mm','observations')
    list_filter = ('manufacturing_date',)
    search_fields = ('n_po',)


