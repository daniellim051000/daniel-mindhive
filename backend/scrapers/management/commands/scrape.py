from django.core.management.base import BaseCommand

from scrapers.utils import CoffeeShopUtils

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # ZusCoffeeView.scrape_address()
        CoffeeShopUtils().scrape_data()
        pass
