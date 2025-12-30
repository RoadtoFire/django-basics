from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome my G!</h1>")

def about(request):
    return HttpResponse("<h2>About Page!</h2>")

def contacts(request):
    return HttpResponse("<h1>Contact List....</h1>")