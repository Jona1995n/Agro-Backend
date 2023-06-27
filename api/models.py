from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField()
    email = models.CharField(max_length=50)
    user = models.CharField(max_length=50)

    def __str__(self):
	    return self.title  

class Facility(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    lon = models.DecimalField(max_digits=10, decimal_places=5, default=0)

    def __str__(self):
        return self.name 