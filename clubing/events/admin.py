
from django.contrib import admin
from .models import Venue, Event, MyClubUser

# Register your models here.

#admin.site.register(Venue)
#admin.site.register(Event)
admin.site.register(MyClubUser)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name","address", "email_address")
    ordering = ('name',)
    search_fields = ("name", "Address")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields  = (("name","venue"), "event_date", 'description', "manager" "attendees")  
    list_display = ("name", "event_date","venue")  
    list_filter = ('event_date','venue')
    ordering  = ('-event_date',)

