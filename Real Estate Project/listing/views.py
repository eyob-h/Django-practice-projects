from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from . import models
from .forms import ListingForm

def view_listings(request):
    listings = models.Listing.objects.all()
    context = {
        'listings': listings
    }

    # return HttpResponse("Listings here")
    return render(request, 'listings/listing.html', context)

def view_single_listing(request, pk):
    listing = models.Listing.objects.get(id=pk)
    context = {
        'listing': listing
    }
    return render(request, 'listings/detail_view.html' , context)

def create_listing(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form,
    }
    return render(request, 'listings/create_listing.html', context)

def update_listing(request, pk):
    listing = models.Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    
    if request.method == 'GET':
        context = {
            'listing':listing,
            'form':form
        }
        # return render(request, '/listings/update_listing.html', context) #THIS DOESN'T WORK!
        return render(request, 'listings/update_listing.html', context)
    else:
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            print(request.POST['title'])
            form.save()
            return redirect('/')


def update_listing1(request, pk):
    listing = models.Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # print(request.POST['title'])
            form.save() 
            return redirect('/')
        
    context = {
        'form': form
    }
    return render(request, 'listings/update_listing.html', context)
        
        
