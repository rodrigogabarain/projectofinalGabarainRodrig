from django.contrib import admin


from planner.models import Planner


@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):
    list_display = ('n_po','date_required','client','raw_material1','finished_product1')
    list_filter = ('date_required',)
    search_fields = ('n_po',)

