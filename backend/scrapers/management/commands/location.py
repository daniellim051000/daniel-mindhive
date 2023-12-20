from django.core.management.base import BaseCommand

from scrapers.location import get_coordinates
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        address = "Blok A, No.5, Tingkat Bawah, Jalan Besar Sura Gate, KPLK Perniagaan Suria Gate, 23000 Dungun, Terengganu Darul Iman"
        get_coordinates(address)
        pass
