from multiprocessing import Event
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect

# Create your views here.

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


#Showing All Types of Events Registered in Database
def all_event(request):
     event = Event.objects.all()
     return render(request, "events/all_event.html", {"event_list":event})

def all_venue(request):
     venue = Venue.objects.all()
     return render(request, "events/all_event.html", {"event_list":venue})     

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
