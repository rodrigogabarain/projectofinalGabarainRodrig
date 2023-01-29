from django import forms

class LogisticForm(forms.Form):
    n_po= forms.CharField(max_length=11,label='N° OP')
    dispatch_date = forms.CharField(max_length=8,label="Fecha de despacho (dd/mm/aa)")
    coh = forms.CharField(max_length=10)
    doh = forms.CharField(max_length=10)
    client = forms.CharField(max_length=30,label='Cliente')
    address = forms.CharField(max_length=30,label='Direccion')
    dispatch = forms.BooleanField(required=False,label='Despachado')
    form_of_dispatch= forms.CharField(max_length=12,label='Forma de despacho')
    item = forms.IntegerField()
    used_raw_material = forms.CharField(max_length=11,label='Materia prima')
    used_raw_material1 = forms.BooleanField(required=False,label='MP descargada')
    used_finished_product = forms.CharField(max_length=15,label='Producto terminado')
    used_finished_product1 = forms.BooleanField(required=False,label='PT descargado')
    observations= forms.CharField(max_length=1500,label='Observaciones')
    firm = forms.CharField(max_length=5,label='Firma')