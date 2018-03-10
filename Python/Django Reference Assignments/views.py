# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "blogs available"
    return HttpResponse(response)

def new(request):
    this = "new blog"
    return HttpResponse(this)

def create(request):
    return redirect('/')

def show(request, number):
    yo = "Placeholder for Blog number " + number
    return HttpResponse(yo) 

def edit(request, number):
    response = "Placeholder to edit Blog number " + number
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')