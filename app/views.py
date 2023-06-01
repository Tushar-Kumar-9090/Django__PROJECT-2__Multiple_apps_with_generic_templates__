from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def first(request):
    return HttpResponse('<h1 style="color: red;"><marquee>This is my first <span style="color:blue;">Django</span> Project</marquee></h1>')

def second(request):
    return HttpResponse('<h1 style="color: red;"><marquee>By Using <span style="color:blue;">HttpResponse</span> We Can Return The String </marquee></h1>')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')