from multiprocessing import Event
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect

# Create your views here.

#function for updating and deleting venues and events
def update_venue(request, venue_id):
     venue = Venue.objects.get(pk=venue_id)
     form = VenueForm(request.POST or None, instance=venue)
     if form.is_valid():
          form.save()
          return redirect("venue-list")
     return render(request, 'events/update_venue.html', {"venue":venue, "form":form}) 

def update_event(request, event_id):
     event = Event.objects.get(pk=event_id)
     form = EventForm(request.POST or None, instance=event)
     if form.is_valid():
          form.save()
          return redirect("event-list")
     return render(request, 'events/update_event.html', {"event":event, "form":form})      


#function for adding more venues and events via website
def add_venue(request):
     submitted  = False
     if request.method == "POST":
          form  = VenueForm(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/add_venue?submitted=True')
     else:          
          form = VenueForm()
          if 'submitted' in request.GET:
               submitted = True
     return render(request, 'events/add_venue.html', {"form":form, "submitted":submitted})


def add_event(request):
     submitted  = False
     if request.method == "POST":
          form  = EventForm(request.POST)
          if form.is_valid(): 
               form.save()
               return HttpResponseRedirect('/add_event?submitted=True')
     else:          
          form = EventForm()
          if 'submitted' in request.GET:
               submitted = True
     return render(request, 'events/add_event.html', {"form":form, "submitted":submitted})  

# Searching for venues 
def search_venues(request):
     if request.method == "POST":
          searched = request.POST['searched']
          venues = Venue.objects.filter(name__contains=searched)
          return render(request, 'events/search_venues.html', {"searched":searched, "venues":venues}) 

     else:
          return render(request, 'events/search_venues.html', {})        


#Showing All Types of Events Registered in Database
def all_event(request):
     event = Event.objects.all()
     return render(request, "events/all_event.html", {"event_list":event})

def all_venue(request):
     venue = Venue.objects.all()
     return render(request, "events/all_venue.html", {"venue_list":venue})    

def show_venue(request, venue_id):
     venue = Venue.objects.get(pk=venue_id)
     return render(request, 'events/show_venue.html', {"venue":venue})      

# Function for First Page of Website
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name="Leela"
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    cal = HTMLCalendar().formatmonth(year, month_number)
    curr_year = datetime.now().year
    return render(request, 'events/home.html',
    {    "name":name,
         "year":year,
         "month": month,
         "cal" : cal,
         "current_year":curr_year,
          
    })
