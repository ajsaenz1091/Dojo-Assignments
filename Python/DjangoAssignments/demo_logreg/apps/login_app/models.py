# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.UserManager):
	def validateRegistration(self):
		errors=[]
		print postData
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

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

	def __str__(self):
		return 'first_name: {}, last_name: {}, email: {}, password: {}'.format(self.first_name, self.last_name)