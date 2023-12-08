from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from challenges.models import MeterPoint, Meter, MeterRegister, Reading
from datetime import datetime


line_026 = ["mpan", "BSC"]
line_028 = ["serial_number"]
line_030 = ["identifier" ,"meter_register", "date", "value"]

class Command(BaseCommand):
    help = 'Read a file and print its content line by line'

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str, help='Path to the file to be read')
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            with open(file_path, 'r') as file:
                for line in file:
                 split_line = line.strip("|\n").split("|")
                 self.stdout.write(str(split_line))
                 if split_line[0] == '026':
                  dictionary = dict(zip(line_026, split_line[1:]))
                  meter_point, created = MeterPoint.objects.get_or_create(mpan = dictionary["mpan"], BSC = dictionary["BSC"])
                  print(dictionary)
                 elif split_line[0] == '028':
                  dictionary = dict(zip(line_028, split_line[1:]))
                  meter, created = Meter.objects.get_or_create(serial_number = dictionary["serial_number"], meter_point = meter_point)
                  print(dictionary)
                 elif split_line[0] == '030':
                  dictionary = dict(zip(line_030, split_line[1:]))
                  date_str = dictionary["date"]
                  date = datetime.strptime(date_str, "%Y%m%d%H%M%S")
                  meter_register = MeterRegister.objects.get_or_create(meter = meter, identifier = dictionary["identifier"])
                  Reading.objects.create(date = datetime.strptime(dictionary["date"],"%Y%m%d%H%M%S"), value = dictionary["value"], flow_filename = file_path)
                  reading, created = Reading.objects.update_or_create(meter_register = dictionary["meter_register"], meter = meter, date = datetime.strptime(dictionary["date"],"%Y%m%d%H%M%S"), defaults={"meter_register": meter_register, "meter": meter, "date": date})
                  print(dictionary) 
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"file not found at path: {file_path}"))
