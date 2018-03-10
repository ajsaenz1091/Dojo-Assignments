# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse, redirect


def index(request):
	if 'couter' not in request.session:
		request.session['number']=0

	return render(request,'surveys/index.html')

def processForm(request):

	request.session['number']+= 1
	

	context = {
		'name' : request.POST['name'],
		'dojoLocation' : request.POST['dojoLocation'],
		'favLang' : request.POST['favLang'],
		'comments' : request.POST['comments']
	}

	print context["name"]
	return render(request,'surveys/result.html',context=context)


