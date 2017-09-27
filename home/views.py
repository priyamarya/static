# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
	
	return render(request,'home.html',{})

def contact(request):
	return  render(request,'contact.html',{})

def faqs(request):
	
	return render(request,'faqs.html',{})

def account(request):
	
	return render(request,'account.html',{})

def about(request):
	
	return render(request,'about.html',{})

def workwithus(request):
	
	return render(request,'workwithus.html',{})
