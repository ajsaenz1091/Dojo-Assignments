# -*- coding: utf-8 -*-
from django.contrib import messages
from time import gmtime, strftime
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

from models import *

def index(request):
	# date = datetime.now().date().strftime('%B %-d, %Y')
	# time = datetime.now().time().strftime('%-I:%M %p')
	time = strftime("%Y-%m-%d %H:%M %p", gmtime())
	
	context = {
		'datetime' : time 
	}
	return render(request,'index.html',context)

