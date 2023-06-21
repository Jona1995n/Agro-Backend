from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Review(models.Model):
	title = models.CharField(max_length=30)
	body = models.TextField()
	time = models.DateTimeField(default=timezone.now)
	name = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title