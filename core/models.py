from django.db import models
from django.contrib.auth import get_user_model
import uuid
import datetime
User = get_user_model()
# Create your models here.
class Create(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=35)
    description = models.TextField()
    due_date = models.DateTimeField(blank=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user
class Contact(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=10000)
    subject = models.CharField(max_length=100)
    message = models.TextField()      

    def __str__(self):
        return self.name
    