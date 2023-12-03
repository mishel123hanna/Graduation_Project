from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Property(models.Model):
    PROPERTY_STATUS = [
        ('RENT', 'For Rent'),
        ('BUY', 'For Sale'),
        ('BOTH', 'For Rent and Sale'),
    ]
    PROPERTY_TYPE = [
        ('شقة', 'Apartment'),
        ('بيت', 'House'),
        ('فندق', 'Hotel'),
        ('أماكن بديلة', 'Alternative Places'),
    ]
    owner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=PROPERTY_STATUS, max_length=4)
    type = models.CharField(choices=PROPERTY_TYPE, max_length=20)
     
    def __str__(self):
        return self.type