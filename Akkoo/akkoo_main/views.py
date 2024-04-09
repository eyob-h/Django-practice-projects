from django.shortcuts import render
from django.http import HttpResponse
from vendors.models import Vendor


def home(request):
    # vendors = Vendor.objects.all()
    vendors = Vendor.objects.filter(is_approved = True, user__is_active = True)[:5]
    context = {
        'vendors':vendors
    }
    return render(request, 'home.html', context)