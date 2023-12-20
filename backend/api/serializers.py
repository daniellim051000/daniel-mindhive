from rest_framework import serializers

from scrapers.models import CoffeeShop

class CoffeeShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeeShop
        fields = ("id","shop_name", "shop_address", "shop_coordinate_latitude", "shop_coordinate_longitude")