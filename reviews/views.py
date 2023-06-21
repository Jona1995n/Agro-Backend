from django.shortcuts import render
from django.http import HttpResponse 
from .models import Review

def home(request):
	context = {
		'title': 'Reviews',
		'reviews': Review.objects.all()
	}

	return render(request, 'Agro/reviews.html', context)

def about(request):
	return render(request, 'Agro/about.html')

