from functools import total_ordering
from operator import concat
from unicodedata import decimal
from django.shortcuts import render
from .models import devices

def home(request):
    return render(request, 'main/Index.html')


def about(request):
    return render(request, 'main/About.html')

def contact(request):
    return render(request, 'main/Contact.html')

def control(request):
    alldevices = list(devices.objects.all())
    return render(request, 'main/control-panel.html',{
        'devices': alldevices,
    })

def login(request):
    return render(request, 'main/login.html')

def details(request, id):
     
    return render(request, 'main/details.html',{
        'device': devices.objects.get(id=id)
    })