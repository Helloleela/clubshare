from xml.parsers.expat import model
from django import forms
from django.forms import ModelForm
from .models import Venue, Event


class EventForm(ModelForm):
    class Meta :
        model = Event

        fields = ("name", "event_date", "venue", "manager","description", "attendees")

        labels = {
            "name": "",
            "event_date":"  ", 
            "venue": "", 
            "manager" :"",
            "description": "", 
            "attendees":"",
            
        }

        widgets = {
              "name" : forms.TextInput(attrs={"class":'form-control', 'placeholder':'Event Name'}),
              "event_date":forms.TextInput(attrs={"class":'form-control','placeholder':'Event Date'}),
              "venue":forms.Select(attrs={"class":'form-select','placeholder':'Event Venue'}),
              "manager":forms.Select(attrs={"class":'form-select','placeholder':'Event Manager'}),
              
              "attendess":forms.SelectMultiple(attrs={"class":'form-control','placeholder':'Attendees'}),
              "description":forms.Textarea(attrs={"class":'form-control','placeholder':'Event Description'}),

        }

class VenueForm(ModelForm):
    class Meta :
        model = Venue

        fields = ("name", "address", "zip_code", "phone","web", "email_address")

        labels = {
            "name": "",
            "address":"  ", 
            "zip_code": "", 
            "phone" :"",
            "web": "", 
            "email_address":"",
            
        }

        widgets = {
              "name" : forms.TextInput(attrs={"class":'form-control', 'placeholder':'Venue Name'}),
              "address":forms.TextInput(attrs={"class":'form-control','placeholder':'Address of Venue'}),
              "zip_code":forms.TextInput(attrs={"class":'form-control','placeholder':'Venue Zip Code'}),
              "phone":forms.TextInput(attrs={"class":'form-control','placeholder':'Contact Number'}),
              "web":forms.TextInput(attrs={"class":'form-control','placeholder':'Web Address'}),
              "email_address":forms.EmailInput(attrs={"class":'form-control','placeholder':'Email Address'}),

        }