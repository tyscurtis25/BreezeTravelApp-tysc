from django.shortcuts import render
from django.http import HttpResponse

from travelsites.models import TripCategory, Destination

# Create your views here.
def showtripsPageView(request) :
    return render(request, 'travelsites/showTrips.html')

def showAfricaPageView(request) :
    id = TripCategory.objects.get(description = "Africa")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showAsiaPageView(request) :
    id = TripCategory.objects.get(description = "Asia")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showAustraliaPageView(request) :
    id = TripCategory.objects.get(description = "Australia")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showEuropePageView(request) :
    id = TripCategory.objects.get(description = "Europe")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showNorthAmericaPageView(request) :
    id = TripCategory.objects.get(description = "North America")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showSouthAmericaPageView(request) :
    id = TripCategory.objects.get(description = "South America")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

