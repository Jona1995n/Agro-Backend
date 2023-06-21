#commit test
from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
	return HttpResponse('<h1>Reviews Home</h1>')

def about(request):
	return HttpResponse('<h1>Reviews About</h1>')