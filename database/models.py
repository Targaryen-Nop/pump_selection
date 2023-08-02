from django.db import models

# Create your models here.


class factory_table(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    fac_number = models.CharField(max_length=20,null=True)
    equipment = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=50, null=True)
    model_short =models.CharField(max_length=20,null=False)
    model = models.CharField(max_length=50,null=True)
    data_type = models.CharField(max_length=10,null=True)
    se_quence = models.IntegerField(null=False)
    rpm = models.IntegerField( null=True)
    imp_dia = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    flow = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    head = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    eff = models.IntegerField(null=True)
    npshr = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    kw = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    curve_format = models.CharField(max_length=20,null=False)
    eff_rl = models.CharField(max_length=10, null=False)
    eff_status = models.IntegerField(null=False)
    eff_distance = models.DecimalField(max_digits=15, decimal_places=4, null=False)
    tolerance = models.IntegerField(null=False)
    scale_xy = models.DecimalField(max_digits=15, decimal_places=4, null=False) 
