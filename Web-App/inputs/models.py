from django.db import models

# Create your models here.

class DairyHerd(models.Model):
    herd_name = models.CharField(max_length=10, default="-")
    herd_size = models.IntegerField(default=0)
    groups = models.IntegerField(default=3)
    def __str__(self):
        return str(self.herd_name)

class DairyCow(models.Model):
    cow_id = models.IntegerField(primary_key=True, unique=True)
    birth_date = models.DateField()
    parity = models.IntegerField(default=1)
    milk_yield = models.FloatField(default=7000)

    def __str__(self):
        description = "cow-{}".format(self.cow_id)
        return description
   
   

