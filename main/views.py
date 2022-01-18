from django.shortcuts import render

def home(request):
    return render(request, 'main/Index.html')


def about(request):
    return render(request, 'main/About.html')

def contact(request):
    return render(request, 'main/Contact.html')

def control(request):
    devices = [
        {'name':'Bedroom 1', 'status':'On', 'slug':'bedroom-1', 'color':'statuson'},
        {'name':'Bedroom 2', 'status':'Off', 'slug':'bedroom-2', 'color':'statusoff'},
        {'name':'Bedroom 3', 'status':'On', 'slug':'bedroom-3', 'color':'statuson'}
    ]
    return render(request, 'main/control-panel.html',{
        'devices': devices,
    })