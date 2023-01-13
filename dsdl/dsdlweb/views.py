from django.shortcuts import render
from .models import Coordinators
# from .models import Coordinators
# Create your views here.

def index(request):
    coordinators=Coordinators.objects.all()
    return render(request,'index.html',{'coordinators':coordinators})

def teams(request):
    coordinators=Coordinators.objects.all()
    return render(request,'teams.html',{'coordinators':coordinators})

def about(request):
    return render(request,'about.html')

def events(request):
    return render(request,'events.html')

def blogs(request):
    return render(request,'blogs.html')

def contact(request):
    return render(request,'contact.html')