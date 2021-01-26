from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Donation(models.Model):
    item = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    date_donated = models.DateTimeField(default=timezone.now)
    donor = models.CharField(max_length=50)

    #return readable object upon query
    def __str__(self):
        return f'{self.donor}-{self.item}'

class Inventory(models.Model):
    item = models.CharField(max_length=50, default='item')
    quantity = models.IntegerField(default=0)

    #return readable object upon query
    def __str__(self):
        return f'{self.item}'