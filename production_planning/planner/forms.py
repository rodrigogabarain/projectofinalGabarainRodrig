from django import forms

from planner.models import Planner

class PlannerForm(forms.Form):
    n_po = forms.CharField(max_length=11, label= 'N° OP')
    admission_date = forms.CharField(max_length=8,label='Fecha de ingreso(dd/mm/aa)')
    client = forms.CharField(max_length=30, label= 'Cliente')
    coh = forms.CharField(max_length=10)
    doh = forms.CharField(max_length=10)
    date_required = forms.CharField(max_length=8,label='Fecha de requerida(dd/mm/aa)')
    dispatch = forms.CharField(max_length=12,label='Forma de despacho')
    item = forms.IntegerField()
    raw_material = forms.CharField(max_length=11,label='Materia prima')
    raw_material1 = forms.BooleanField(required=False,label='MP en stock')
    finished_product = forms.CharField(max_length=15,label='Producto terminado')
    finished_product1 = forms.BooleanField(required=False,label='PT en stock')
    
