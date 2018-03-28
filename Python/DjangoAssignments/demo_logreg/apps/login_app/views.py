
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import User

def index(request):
	return render(request, 'login_app/index.html')
def register(request):
	#validation
	#check to see what response was
	#if respose good then

	isValid = True
	if len(request.POST['first_name'])<3:
		print "first name not long enough"
	if len(request.POST['last_name'])<3:
		print "last name not long enough"

	if len(errors):
		for error in errors:
			message.error(request,error)
		return redirect('/')
	new_user = User.objects.create(
		first_name = request.POST['first_name'],
		last_name= request.POST['last_name'],
		email= request.POST['email'],
		password= request.POST['password']
		)
	request.session['user_id']= new_user.id 
	print request.POST
	return redirect('/')

def login(request):
	errors = []
	existing = User.objects.filter(email=request.POST['email'])
	if len(existing)< 1



def success(request):
	if 'user_id' not in request.session
		return redirect('/')
	context = {
		'user' : User.objects.get(id=request.session['user_id'])
	}
	return render(request, 'login_app/success.html', context)

