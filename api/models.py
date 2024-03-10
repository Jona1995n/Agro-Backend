from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

class Facility(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    email_address = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=20, decimal_places=15, default=0)
    lon = models.DecimalField(max_digits=20, decimal_places=15, default=0)

    @property
    def reviews(self):
        return self.review_set.all()

    def __str__(self):
        return self.name

class Review(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=30)
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField()
    email = models.CharField(max_length=50)
    user = models.CharField(max_length=50)

    class Meta:
        unique_together = ("facility", "user")

    def __str__(self):
	    return self.title