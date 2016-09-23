from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return HttpResponse(render(request,'index.html'))

def cows(request):
  return HttpResponse("Hello, world. This is the cows form")

def no_page(request):
  return HttpResponse("Sorry this page does not exist yet")
