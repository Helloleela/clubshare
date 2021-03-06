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

    #Searching venue via search bar
    path("search_venue", views.search_venues, name="search-venue"),


    # Updating and deleting Venues and Events 
    path("update_venue/<venue_id>", views.update_venue, name="update-venue"),
    path("delete_venue/<venue_id>", views.delete_venue, name="delete-venue"),

    path("update_event/<event_id>", views.update_event, name="update-event"),
    path("delete_event/<event_id>", views.delete_event, name="delete-event"),

    #Downloading Venue-list in form of text and CSV file
    path("venue_text", views.venue_text, name="venue-text"),
    path("venue-csv", views.venue_csv, name="venue-csv"),
]