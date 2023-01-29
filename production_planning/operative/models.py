from django.db import models


class Operative(models.Model):
    n_po= models.CharField(max_length=11,verbose_name="N°OP")
    production_entry_date = models.CharField(max_length=8,verbose_name="Ingraso a produccion (dd/mm/aa)")
    manufacturing_date = models.CharField(max_length=8,verbose_name="Fecha mecanizado (dd/mm/aa)")
    item = models.IntegerField()
    used_raw_material = models.CharField(max_length=11,verbose_name="Material utilizado")
    mp_mm = models.FloatField()
    used_finished_product = models.CharField(max_length=11,verbose_name="Producto terminado utilizado")
    pt_mm = models.FloatField()
    observations= models.CharField(max_length=1500,verbose_name="Observaciones")
    firm = models.CharField(max_length=5,verbose_name="Firma")


    def __str__(self):
        return self.n_po

    
    
    class Meta:
        verbose_name = 'Operario'
        verbose_name_plural ='Operarios'    