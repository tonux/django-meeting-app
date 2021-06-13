from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse("Welcome to my website")

def index(request):
    return HttpResponse("Page index")
