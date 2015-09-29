from django.db import models
from accounts.models import UserProfile

# Create your models here.
class Bill(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    shared_with = models.ManyToManyField(UserProfile, blank=True)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    bill = models.ForeignKey(Bill, blank=True, null=True, related_name='items')
    
    def __str__(self):
        return self.name
        
