from django.db import models
from django.contrib.auth.models import User


default_user = User.objects.first()

# Create your models here.
class Interaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_input = models.TextField() 
    ai_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Interaction at {self.timestamp} - User input: {self.user_input[:50]}"
    
    class Meta:
        ordering = ['-timestamp']


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
    
    
class Feed(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='uploads/product/')
    
    def __str__(self):
        return self.title