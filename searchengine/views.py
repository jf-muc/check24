from datetime import date
from django.shortcuts import render

from .models import Offer
from .backend__results import Data


def serachView(request):

    airports = []
    for airport in Offer.objects.all().values('outbounddepartureairport').iterator():
        airports.append(airport.get('outbounddepartureairport'))
    airports = list(dict(dict.fromkeys(airports)))

    return render(request, 'searchengine/index.html', {
        'airports': airports
    })

def resultView(request, searchURL):
    filters = Data(searchURL)
    filteredObjects = filters.searchOffers()
    airports = []
    for airport in Offer.objects.all().values('outbounddepartureairport').iterator():
        airports.append(airport.get('outbounddepartureairport'))
    airports = list(dict(dict.fromkeys(airports)))
    return render(request, 'searchengine/results.html',  {
        'filteredObjects': filteredObjects,
        'duartion': filters.getDuration(),
        'today': date.today().strftime("%Y-%m-%d"),
        'dataDict': filters.get_optimized_DataDict(),
        'airports': airports,
        'hotels': filters.searchHotels(filteredObjects)
    })

def bookingView(request, bookingHotelID):
    hotelNr = bookingHotelID[8:]
    hotel = list(Offer.objects.all().filter(Hotel_ID=hotelNr).values())
    print(hotel)
    return render(request,'searchengine/booking.html', {
        'hotel': hotel[0]
    })