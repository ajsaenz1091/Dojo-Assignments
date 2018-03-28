
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def register(request):
	return HttpResponse('placeholder for users to create a new user record')

def login(request):
	return HttpResponse('placeholder for user login')
def users(request):
	return HttpResponse('placeholder to later display all the list of users')
