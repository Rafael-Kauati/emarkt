from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def greet(request):
    return render(request, 'greet.html')
