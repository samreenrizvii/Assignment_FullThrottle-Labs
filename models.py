from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
     id = models.CharField(max_length=10)
     real_name = models.CharField(max_length=20)
     tz = models.TextField(max_length=100) 
     one = models.DateTimeField(default=timezone.now)
     two = models.DateTimeField(default=timezone.now)
     three = models.DateTimeField(default=timezone.now)



