# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse, redirect
from time import localtime, strftime, gmtime

# Create your views here.

def index(request):
	return render(request, 'session_word/index.html')

def process(request):
	
	my_word = {
	'text' : request.POST['new_word'],
	'color' : request.POST['chosen_color'],
	'font' : request.POST['font'],
	'Datetime': strftime("%H:%M:%Spm %d %b %Y",gmtime())

	}


	if 'word_list' not in request.session:
		request.session['word_list'] = []
	else:
	#this else statement logic all it's doing is adding the new word to the list.
		list = request.session['word_list']
		list.append(my_word)
		request.session['word_list']= list

	return redirect('/')
def clear(request):
	request.session.clear()
	return redirect(request,'/')


