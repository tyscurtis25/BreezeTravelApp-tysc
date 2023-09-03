from django.shortcuts import render
from django.http import HttpResponse

from travelsites.models import TripCategory, Destination

# Create your views here.
def showtripsPageView(request) :
    return render(request, 'travelsites/showTrips.html')

def showAfricaEgyptPageView(request) :
    id = TripCategory.objects.get(description = "Africa: Egypt")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "africa1-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showAfricaTanzaniaPageView(request) :
    id = TripCategory.objects.get(description = "Africa: Tanzania")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "africa2-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showAsiaChinaPageView(request) :
    id = TripCategory.objects.get(description = "Asia: China")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "asia1-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showAsiaIndonesiaPageView(request) :
    id = TripCategory.objects.get(description = "Asia: Indonesia")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "asia2-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showAsiaJapanPageView(request) :
    id = TripCategory.objects.get(description = "Asia: Japan")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "asia3-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showAustraliaPageView(request) :
    id = TripCategory.objects.get(description = "Australia")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "australia-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showCentralAmericaPageView(request) :
    id = TripCategory.objects.get(description = "Central America: Mexico")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "centralamerica-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showEuropeFrancePageView(request) :
    id = TripCategory.objects.get(description = "Europe: France")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "europe1-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showEuropeItalyPageView(request) :
    id = TripCategory.objects.get(description = "Europe: Italy")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "europe2-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showMiddleEastPageView(request) :
    id = TripCategory.objects.get(description = "Middle East: UAE")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "middleeast-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showNorthAmericaArizonaPageView(request) :
    id = TripCategory.objects.get(description = "North America: Arizona")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "northamerica1-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showNorthAmericaHawaiiPageView(request) :
    id = TripCategory.objects.get(description = "North America: Hawaii")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "northamerica2-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showSouthAmericaArgBrazilPageView(request) :
    id = TripCategory.objects.get(description = "South America: Argentina-Brazil")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "southamerica1-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showSouthAmericaBrazilPageView(request) :
    id = TripCategory.objects.get(description = "South America: Brazil")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "southamerica2-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})

def showSouthAmericaPeruPageView(request) :
    id = TripCategory.objects.get(description = "South America: Peru")
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "title" : data.title,
        "description" : data.description,
        "image1" : data.main_photo,
        "image2" : data.second_photo,
        "image3" : data.third_photo
    }
    background_class = "southamerica3-bg"
    return render(request, 'travelsites/displaytrips.html', {'background_class': background_class, 'context': context})
