from django.db import models


class Planner(models.Model):
    CHOICE_DISPATCH = (
        ('consolidated', 'consolidado'),
        ('bus', 'micro'),
        ('withdraw', 'retira'),        
    )
    
    n_po= models.CharField(max_length=11,verbose_name="N°OP")
    admission_date = models.CharField(max_length=8,verbose_name="Fecha de ingreso(dd/mm/aa)")
    client = models.CharField(max_length=30,verbose_name="Cliente")
    coh = models.CharField(max_length=10)
    doh = models.CharField(max_length=10)
    date_required = models.CharField(max_length=8,verbose_name="Fecha de requerida(dd/mm/aa)")
    dispatch = models.CharField(max_length=12, choices = CHOICE_DISPATCH , default='consolidated')
    item = models.IntegerField()
    raw_material = models.CharField(max_length=11,verbose_name="Materia Prima")
    raw_material1 = models.BooleanField(default=True,verbose_name="MP en Stock")
    finished_product = models.CharField(max_length=15,verbose_name="Producto Terminado")
    finished_product1 = models.BooleanField(default=True,verbose_name="PT en Stock")
    


    def __str__(self):
        return f'{self.n_po} -{self.client}'
    
    class Meta:
        verbose_name = 'Planificador'
        verbose_name_plural ='Planificadores'    