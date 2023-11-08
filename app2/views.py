from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jampandu1(request):
    return HttpResponse('hi jampandu how r u want to meet u once')
def pyspiders(request):
    return HttpResponse('<h1><marquee>we are under pressure</h1></marquee>')
