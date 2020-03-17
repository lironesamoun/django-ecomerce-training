from django.db import models

# Create your models here.


class Item(models.Model):
    pass

# Link the item with the order itself
class OrderItem(models.Model):
    pass


class Order(models.Model):
    pass
