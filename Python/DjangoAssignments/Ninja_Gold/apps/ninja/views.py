# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse, redirect
from random import *
from time import localtime, strftime, gmtime

# Create your views here.

def index(request):
	if 'gold' not in request.session:
		request.session['gold']=0
		request.session['log']=[]
	return render(request,'ninja/index.html')

def process(request):
	if request.POST['findGold'] == 'farm':
		golds = randint(10,20)
		request.session['gold']+= golds
		request.session['log'].append('earned '+ str(golds)+ ' golds from the farm ' + (strftime("%H:%M:%Spm %d %b %Y",gmtime()))) 
	elif request.POST['findGold']=='cave':
		golds = randint(5,10)
		request.session['gold']+= golds
		request.session['log'].append('earned '+ str(golds) + ' golds from the cave ' + (strftime("%H:%M:%Spm %d %b %Y",gmtime())))
	elif request.POST['findGold']=='house':
		golds = randint(2,5)
		request.session['gold']+= golds
		request.session['log'].append('earned '+ str(golds)+ ' golds from the house ' + (strftime("%H:%M:%Spm %d %b %Y",gmtime())))
	elif request.POST['findGold']=='casino':
		golds = randint(-50,50)
		request.session['gold']+= golds
		if golds >=0:
			request.session['log'].append('earned '+ str(golds)+ ' golds from the casino ' + (strftime("%H:%M:%Spm %d %b %Y",gmtime())))
		else:
			request.session['log'].append('Entered a casino and lost '+ str(golds) + 'golds... Ouch.. ' + (strftime("%H:%M:%Spm %d %b %Y",gmtime())))



	return redirect(index)



def clear(request):
	request.session.clear()
	return redirect('/')