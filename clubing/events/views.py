from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.

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
