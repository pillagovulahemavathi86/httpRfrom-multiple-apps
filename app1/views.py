from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first1(request):
    return HttpResponse('this is first view of app1')

def second1(request):
    return HttpResponse('<h1> this is second view of app1</h1>')
