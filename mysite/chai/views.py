from django.shortcuts import render
from .models import ChaiTypes

# Create your views here.
def all_chai(request) :
    chais = ChaiTypes.objects.all()
    return render(request,'chai/all_chai.html',{'chais' : chais})


