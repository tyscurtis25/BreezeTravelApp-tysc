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
        "title" : data.title,
        "image1" : data.main_photo,
        "image2" : data.secondary_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showAsiaPageView(request) :
    id = TripCategory.objects.get(description = "Asia")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "image1" : data.main_photo,
        "image2" : data.secondary_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showAustraliaPageView(request) :
    id = TripCategory.objects.get(description = "Australia")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "image1" : data.main_photo,
        "image2" : data.secondary_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showEuropePageView(request) :
    id = TripCategory.objects.get(description = "Europe")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "image1" : data.main_photo,
        "image2" : data.secondary_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showNorthAmericaPageView(request) :
    id = TripCategory.objects.get(description = "North America")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "image1" : data.main_photo,
        "image2" : data.secondary_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showSouthAmericaPageView(request) :
    id = TripCategory.objects.get(description = "South America")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "image1" : data.main_photo,
        "image2" : data.secondary_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showMiddleEastPageView(request) :
    id = TripCategory.objects.get(description = "Middle East")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "image1" : data.main_photo,
        "image2" : data.secondary_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

