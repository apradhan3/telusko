from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.img = 'destination_1.jpg'
    # dest1.desc = 'The City That Never Sleeps'
    # dest1.price = 700
    # dest1.offer = True
    
    # dest2 = Destination()
    # dest2.name = 'Atlanta'
    # dest2.img = 'destination_2.jpg'
    # dest2.desc = 'My first Home.'
    # dest2.price = 1000
    # dest2.offer = False
    
    # dest3 = Destination()
    # dest3.name = 'Mechanicburg'
    # dest3.img = 'destination_3.jpg'
    # dest3.desc = 'The City That Made Me Rich.'
    # dest3.price = 700
    # dest3.offer = False 
    
    # dests = [dest1,dest2,dest3]
    
    dests = Destination.objects.all()
    
    return render(request,"index.html", {'dests': dests})