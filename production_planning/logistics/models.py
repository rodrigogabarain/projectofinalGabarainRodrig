from django.db import models


class Logistics(models.Model):
    DISPATCH = (
        ('consolidado', 'consolidado'),
        ('micro', 'micro'),
        ('retira', 'retira'),        
    )

    n_po= models.CharField(max_length=11,verbose_name="N°OP")
    dispatch_date = models.CharField(max_length=8,verbose_name="Fecha de despacho (dd/mm/aa)")
    coh = models.CharField(max_length=10)
    doh = models.CharField(max_length=10)
    client = models.CharField(max_length=30,verbose_name="Cliente")
    address = models.CharField(max_length=30,verbose_name="Direccion")
    dispatch = models.BooleanField(default=True,verbose_name="Despachado")
    form_of_dispatch= models.CharField(max_length=12, choices = DISPATCH,verbose_name="Forma de despacho")
    item = models.IntegerField()
    used_raw_material = models.CharField(max_length=11,verbose_name="Materia prima")
    used_raw_material1 = models.BooleanField(default=True,verbose_name="Materia prima descargada")
    used_finished_product = models.CharField(max_length=15,verbose_name="Producto terminado")
    used_finished_product1 = models.BooleanField(default=True,verbose_name="Producto terminado descargado")
    observations= models.CharField(max_length=1500,verbose_name="Observaciones")
    firm = models.CharField(max_length=5,verbose_name="Firma")
    


    def __str__(self):
        return self.n_po
    
    class Meta:
            verbose_name = 'Logistico'
            verbose_name_plural ='Logisticos'    