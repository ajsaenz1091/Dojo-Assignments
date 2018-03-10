from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
   print strftime("%y-%m-%d %H:%M:%S", gmtime())
   print get_random_string(length=14)

   return HttpResponse(response)

def new(request):
	
	return render(request, 'blogs/new.html')

def show(request, id):

	return render(request, 'blogs/show.html', {"blogs": Blog.objects.get(id=id)})

def edit(request, id):

	return render(request, 'blogs/edit.html', {"blog": Blog.objects.get(id=id)})

def update(request, id):

	errors = Blog.objects.basic_vaidator (request.POST)
	if len(errors):
		for tag in errors.iteritems():