from django.shortcuts import render, HttpResponse

# Create your views here.
from . import models

def view_listings(request):
    listings = models.Listing.objects.all()
    context = {
        'listings': listings
    }

    # return HttpResponse("Listings here")
    return render(request, 'listings/listing.html', context)