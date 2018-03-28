# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def welcome(request):
	return render(request,'belt_app/welcome.html')

def logout(request):
	request.session.clear()
	return redirect('/')
def posts(request):
	return render(request, 'belt_app/posts.html')

def quote(request):
	