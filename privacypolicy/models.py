from django.db import models

class PrivacyPolicy(models.Model):
	privacyPolicy = models.CharField(max_length=30)

	def __str__(self):
		return self.title

