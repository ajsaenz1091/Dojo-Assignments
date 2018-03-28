# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
	def register_validation(self,postData):
		errors=[]
		if not postData['name'].isalpha():
			errors.append("Name must be all Alpha charaters")
			print "Name must be all Alpha charaters"
		#look at the database check if alias is in database, if so, not valid
		if len(User.objects.filter(alias=postData['alias']))>0:
			errors.append("Alias must be unique user alias already in use")
			print "Alias must be unique user alias already in use"
		#look at the database check if email is in database, if so, not valid
		if len(User.objects.filter(email=postData['email']))>0:
			errors.append("email must be unique user email already in use")
			print "email must be unique user email already in use"
		#does password and confirmation equal eachother, and 8 characters or more?, if so, valid
		if postData['password'] != postData['confirmation']:
			errors.append("confirmation does not match password")
		if len(postData['password']) < 8:
			errors.append("password must be at least 8 characters")
		if not EMAIL_REGEX.match(postData['email']):
			errors.append("enter email in correct format")
			print "Invalid Email Address!"
		if len(errors) == 0:
			User.objects.create(name=postData['name'],alias=postData['alias'],email=postData['email'], birthday=postData['birthday'], password=postData['password'])
		else:
			return errors

	def login(self,postData):
		errors=[]
		user_list = User.objects.filter(email =postData['email'])
		if len(user_list)<1:
			print 'email was invalid'
			erros.append('Invalid email')
			return errors
		if postData['password'] != user_list[0].password:
			print "password doesn't match"
			errors.append('You have entered an invalid email / password')
		return errors



# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=255)
	alias=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	birthday = models.DateField()
	objects = UserManager()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return '<id: {}, name: {}, alias: {}, email: {}, birthday: {}>'.format(self.id,self.name, self.alias, self.email, self.birthday)


class Quote(models.Model):
	author = models.CharField(max_length=255)
	desc = models.TextField(max_length=255)
	#the line bellow creates a one to many relationship between User and Quote
	creator = models.ForeignKey(User, related_name="quotes")
	#the nex line creates a Many to Many relationship between User and Quote
	#by creating a third table called favorites.
	# objects = models.QuoteManager()
	favorites = models.ManyToManyField(User, related_name="favorited_quotes")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return '<id: {},author: {}, desc: {},creator: {} >'.format(self.id,self.desc,self.author)
		