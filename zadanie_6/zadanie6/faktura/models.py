from django.db import models


class Invoice(models.Model):
    date_of_payment = models.DateField()
    companys_name = models.CharField(max_lenght=255)
    quota = models.IntegerField(max_digits=50, decimal_places=2)
    paid = models.BooleanField(default=False)
