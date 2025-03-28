from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/',null=True,blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.username
    
