from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    text = "<h1>Hello from DJANGO</h1>"
    return HttpResponse(text)