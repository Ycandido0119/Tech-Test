from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = 'Read a file and print its content line by line'

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str, help='Path to the file to be read') 