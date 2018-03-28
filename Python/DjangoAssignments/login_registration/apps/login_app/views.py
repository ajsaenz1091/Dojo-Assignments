# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages	

# Create your views here.
#This is the root route
def index(request):
	return render(request,'login_app/index.html')
#This is the register route
def register(request):
	errors = User.objects.register_validation(request.POST)
	if len(errors) == 0:
		request.session['id']=User.objects.get(email=request.POST['email']).id
		return redirect('/success')
	for error in errors:
		messages.add_message(request, messages.INFO,error)
	return redirect('/')

def success(request):
	return render(request,'login_app/success.html')

def login(request):
	errors = User.objects.login(request.POST)
	#This is checking if there were errors returned
	if len(errors) == 0:
		request.session['id']=User.objects.get(email=request.POST['email']).id
		return redirect('/success')
	for error in errors:
		messages.add_message(request, messages.INFO,error)
	return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')