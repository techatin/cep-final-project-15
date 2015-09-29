from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='userimg/', blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name='sharers')
    
    def __str__(self):
        return self.user.username
