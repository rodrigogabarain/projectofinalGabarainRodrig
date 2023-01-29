from django import forms

class OperativeForm(forms.Form):
    n_po= forms.CharField(max_length=11)
    production_entry_date = forms.CharField(max_length=8)
    manufacturing_date = forms.CharField(max_length=8)
    item = forms.IntegerField()
    used_raw_material = forms.CharField(max_length=11)
    mp_mm = forms.FloatField()
    used_finished_product = forms.CharField(max_length=11)
    pt_mm = forms.FloatField()
    observations= forms.CharField(max_length=1500)
    firm = forms.CharField(max_length=5)