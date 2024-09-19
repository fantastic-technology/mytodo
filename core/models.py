from django.db import models
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()
# Create your models here.
class Create(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=35)
    description = models.TextField()
    due_date = models.TimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user