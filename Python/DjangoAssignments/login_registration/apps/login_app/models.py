# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
	def register_validation(self, postData):
		errors =[]
		#name can not be numbers
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
			errors.append("password must be at least 9 characters")
		if not EMAIL_REGEX.match(postData['email']):
			errors.append("enter email in correct format")
			print "Invalid Email Address!"
		if len(errors) == 0:
			User.objects.create(name=postData['name'],alias=postData['alias'],email=postData['email'], password=postData['password'])
		print "*************"
		print errors
		print "*************"
		return errors

	def login(self, postData):
		errors = []
		user_list = User.objects.filter(email=postData['email'])
		#take info form the form, look for email in database
		if len(user_list) < 1:
			errors.append("You have entered an invallid email") 
			return errors
		if postData['password'] != user_list[0].password:
			errors.append("You have entered an invalid email / password")
		return errors


		#check if email in database 
		#check if password matches



class User(models.Model):
	name = models.CharField(max_length=255)
	alias=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
	def __repr__(self):
		return '<id: {}, name: {}, alias: {}, email: {}>'.format(self.id,self.name, self.alias, self.email)

class Book(models.Model):
	title = models.CharField(max_length=255)

	def __repr__(self):
		return '<id: {}, title: {}>'.format(self.id,self.title)

class Review(objects)
	rating =.models