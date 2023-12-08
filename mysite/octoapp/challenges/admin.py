from django.contrib import admin
from .models import MeterPoint, Meter, Reading



class MeterpointAdmin(admin.ModelAdmin):
    search_fields = ['mpan', 'BSC']

class MeterAdmin(admin.ModelAdmin):
    search_fields = ['serial_number', 'meter_point']

class ReadingAdmin(admin.ModelAdmin):
    list_display = ['value', 'date', 'serial_number', 'mpan']
    search_fields = ['meter__serial_number', 'meter__meter_point__mpan']        

admin.site.register(MeterPoint, MeterpointAdmin)
admin.site.register(Meter, MeterAdmin)
admin.site.register(Reading, ReadingAdmin)