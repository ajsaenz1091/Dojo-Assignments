# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'belt_app/index.html')

def register(request):
	errors = User.objects.register_validation(request.POST)
	if len(errors) == 0:
		request.session['id']=User.objects.get(email=request.POST['email']).id
		return redirect('/success')
	for error in errors:
		messages.add_message(request, messages.INFO,error)
	return redirect('/')

def welcome(request):
	return render(request,'belt_app/welcome.html')

def success(request):
	return HttpResponse('success')
	return redirect ('/')

def login(request):
	errors = User.objects.login(request.POST)
	#This is checking if there were errors returned
	if len(errors) == 0:
		request.session['id']=User.objects.get(email=request.POST['email']).id
		request.session['name']=User.objects.get(email=request.POST['email']).name
		return redirect('/welcome')
	for error in errors:
		messages.add_message(request, messages.INFO,error)
	return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')

def posts(request):
	return render(request, 'belt_app/posts.html')


def new_quote(request):
	Quote.objects.register_quote(request.POST)
	return redirect('/welcome')