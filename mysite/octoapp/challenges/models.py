from django.db import models

class MeterPoint(models.Model):
    mpan = models.CharField(max_length=30)
    BSC = models.CharField(max_length=30)
class Meter(models.Model):
    serial_number = models.CharField(max_length=30)
    meter_point = models.ForeignKey(MeterPoint, on_delete=models.CASCADE)
class MeterRegister(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=30)
class Reading(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    flow_filename = models.CharField(max_length=100)
    meter_register = models.ForeignKey(MeterRegister, on_delete=models.CASCADE)  
    @property
    def serial_number(self):
        return self.meter.serial_number   
    
    @property
    def mpan(self):
        return self.meter.meter_point.mpan
# Create your models here.
