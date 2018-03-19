
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Hello, I am blogs!"
	return HttpResponse(response)
def new(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)
def create(request):
  	return redirect('/')
def show(request,number):
	print number
	return HttpResponse("show method"+ number)
def edit(request, number):
	print number
	return HttpResponse("Edit"+ number)
def delete(request, number):
	print number
	return HttpResponse("Delete" + number)
def blogs(request):
	return HttpResponse('placeholder to later display all the list of blogs')
def surveys(request):
	return HttpResponse('placeholder to display all the surveys created')
def register(request):
	return HttpResponse('placeholder for users to create a new user word')
