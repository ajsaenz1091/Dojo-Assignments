
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return HttpResponse('placeholder to later display all the list of blogs')
def new(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)
def create(request):
  	return redirect('/blogs')
def show(request,number):
	print number
	return HttpResponse("placeholder to display blog"+ number)
def edit(request, number):
	print number
	return HttpResponse("placeholder to edit blog"+ number)
def destroy(request, number):
	return redirect('/blogs')
