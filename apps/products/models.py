from django.db import models


class Produtcs(models.Model):
    MEASUREMENT_CHOICES = [
        ('Unidade', 'unid'),
        ('Dúzia', 'dz'),
        ('Quilo', 'kg'),
        ('Litro', 'l'),
        ('Peça', 'pç'),
        ('Pedaç', 'pdç'),
        ('Caixa', 'cx'),
    ]
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(default='')
    units_measurement = models.CharField(max_length=10, choices=MEASUREMENT_CHOICES)
    purchase_price = models.FloatField(default=0.00)
    sale_price = models.FloatField(default=0.00)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    stock = models.BooleanField(default=False)


    def __str__(self):
        return self.name