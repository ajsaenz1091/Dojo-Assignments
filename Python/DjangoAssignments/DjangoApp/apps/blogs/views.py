
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
