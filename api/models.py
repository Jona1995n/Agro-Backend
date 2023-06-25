from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    lon = models.DecimalField(max_digits=10, decimal_places=5, default=0)

    def __str__(self):
        return self.name

class Review(models.Model):
	title = models.CharField(max_length=30)
	body = models.TextField()
	time = models.DateTimeField(default=timezone.now)
	time = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title