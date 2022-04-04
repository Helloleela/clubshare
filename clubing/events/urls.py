from unicodedata import name
from django.urls import path 
from . import views 

urlpatterns = [ 
    path("", views.home, name ="home"),
    path("<int:year>/<str:month>", views.home, name ="home"),

    # Showing All Events And Venues Available in database
    path("event_list", views.all_event, name="event-list"),
    path("venue_list", views.all_venue, name="venue-list"),
    path("show_venue/<venue_id>", views.show_venue, name="show-venue"),


    #Adding more venues from website
    path("add_venue",views.add_venue, name='add-venue'),
    path("add_event", views.add_event, name='add-event'),
]