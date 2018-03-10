# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
	if 'number' not in request.session:
		request.session['number']=0

	return  render(request,'Random_Word_app/index.html') 

def random_word(request):

	request.session['number']+=1
	request.session['word']= get_random_string(length=14)
	return redirect('/')