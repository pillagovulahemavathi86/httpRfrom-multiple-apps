from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('this first view of app')
def second(request):
    return HttpResponse('<h1>this is second view of app</h1>')
