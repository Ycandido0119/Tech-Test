from django.db import models

class MeterPoint(models.Model):
    mpan = models.CharField(max_length=30)

class Meter(models.Model):
    serial_number = models.CharField(max_length=30)
    meter_point = models.ForeignKey(MeterPoint, on_delete=models.CASCADE)

class Reading(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    flow_filename = models.CharField(max_length=100)     

# Create your models here.
