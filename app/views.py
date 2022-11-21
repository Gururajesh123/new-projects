from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<marquee>This is our first view function</marquee>')

def second(request):
    return HttpResponse('This is our second view function')

def propose(request):
    return HttpResponse('Yes I Love U')

def reject(request):
    return HttpResponse('Akka chellellu lera ra neku')