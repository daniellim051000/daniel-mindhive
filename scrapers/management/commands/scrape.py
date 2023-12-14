from django.core.management.base import BaseCommand

from scrapers.views import ZusCoffeeView
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # ZusCoffeeView.scrape_address()
        ZusCoffeeView().scrape_data()
        pass
