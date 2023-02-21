from django.http import HttpResponse
from django.shortcuts import render

def homedef(request):
    return HttpResponse('<h1>Home page</h1>')


def cardef(request, brand='choice', model='choice', year='choice'):
    return HttpResponse(f'<h1>brand: {brand}</h1><h2> model: {model}</h2><h3>year: {year}</h3>')
# Create your views here.
