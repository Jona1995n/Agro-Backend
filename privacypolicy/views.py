from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
	context = {
		'title': 'Privacy Policy'
	}

	return render(request, 'Agro/privacypolicy.html', context)


