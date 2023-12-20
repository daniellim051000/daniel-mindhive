from rest_framework import routers

from api.views import CoffeeShopAPIViewSet

router = routers.SimpleRouter()
router.register(r"shop", CoffeeShopAPIViewSet, "shop")

urls = []

urls += router.urls