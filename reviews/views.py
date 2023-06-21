from django.shortcuts import render
from django.http import HttpResponse 

reviews = [
	{
  		"body": "Ty yuuuu teeth kitty Uighur ewryub Kiki dusty jujus huiii ffghhh ccddjk kkkkjbbdd Ruth just gddgii",
  		"email": "j@n-com",
  		"name": "Jona Nunez",
  		"stars": 3,
  		"time": 1686539559,
  		"title": "Ok!!!!!"
	},
	{
  		"body": "yerrrrrrrrrrrr",
  		"email": "j@n-com",
  		"name": "Jona Nunez",
  		"stars": 5,
  		"time": 1686539400,
  		"title": "Ok!!!!!"
	}
]

def home(request):
	context = {
		'title': 'Reviews',
		'reviews': reviews
	}

	return render(request, 'Agro/reviews.html', context)

def about(request):
	return render(request, 'Agro/about.html')

