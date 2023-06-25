from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Review(models.Model):
	reviewBody = models.CharField(max_length=30)

	def __str__(self):
		return self.title

