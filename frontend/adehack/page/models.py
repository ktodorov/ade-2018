from django.db import models

class Supplier(models.Model):
    supplier = models.CharField(max_length=100)
    address = models.CharField(max_length=200)