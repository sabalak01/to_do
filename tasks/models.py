from django.db import models
from users.models import CustomUser

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('completed', 'Выполнено'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    
    
    def __str__(self):
        return self.title
