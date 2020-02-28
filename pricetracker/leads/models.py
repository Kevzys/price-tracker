from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="productlist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    connctedlist = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    update = models.BooleanField(default=True)

    def __str__(self):
        return "Item: " + self.name + " Price: " + str(self.price)