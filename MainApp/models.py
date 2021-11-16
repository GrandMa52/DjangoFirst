from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=40)
    quantity = models.PositiveIntegerField()
