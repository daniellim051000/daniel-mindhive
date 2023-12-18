from django.db import models

# Create your models here.)
class CoffeeShop(models.Model):
    shop_name = models.CharField(max_length=200)
    shop_address = models.CharField(max_length=255)
    shop_coordinatez_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    shop_coordinatez_longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.shop_name
    
    class Meta:
        db_table = "coffee_shop"
        verbose_name = "Coffee Shop"
        verbose_name_plural = "Coffee Shops"