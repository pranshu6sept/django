from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. you are at chai and code Home Page")
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'about/index.html')

def contact(request):
    return render(request, 'contact/index.html')