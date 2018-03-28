# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'login_reg_app/index.html')

def register(request):
	results = User.objects.register_validation(request.POST)
	if len(results)<1:
		messages.add_message(request, messages.INFO,'succesful registration!')
		return redirect('/')
	else:
		for error in results:
			messages.add_message(request, messages.INFO,error)
		return redirect('/')

def login(request):
	results = User.objects.login(request.POST)
	if len(results)<1:
		return redirect('/belt_app/welcome')
	else:
		return HttpResponse('whatever')

def logout(request):
	request.session.clear()
	return redirect('/')

def posts(request):
	return render(request, 'belt_app/posts.html')
