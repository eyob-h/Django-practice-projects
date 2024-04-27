from django.shortcuts import render
from vendors.models import Vendor
# Create your views here.

def marketplace(request):
    vendors = Vendor.objects.filter(is_approved = True, user__is_active = True)
    vendor_count = vendors.count()
    context = {
        'vendors':vendors,
        'vendors_count':vendor_count
    }
    return render(request, 'marketplace/listings.html', context)