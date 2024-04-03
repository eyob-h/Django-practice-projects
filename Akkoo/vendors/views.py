from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from accounts.forms import UserProfileForm
from vendors.forms import VendorForm

from accounts.models import UserProfile
from vendors.models import Vendor

from django.contrib import messages

from django.contrib.auth.decorators import login_required, user_passes_test

from accounts.views import check_role_vendor

from menu.models import Category, FoodItem

#get vendor helper function
def get_vendor(request):
    vendor = Vendor.objects.get(user = request.user)
    return vendor

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vprofile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)


    profile_form = UserProfileForm(instance=profile)
    vendor_form = VendorForm(instance=vendor)
    


    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=vendor)

        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, "Profile Updated Successfuly")
            return redirect('vprofile')
        else:
            print(profile_form.errors)
            print(vendor_form.errors)
    else:
        vendor_form = VendorForm(instance=vendor)
        profile_form = UserProfileForm(instance=profile)


    context = {
        'profile_form':profile_form,
        'vendor_form':vendor_form,
        'profile':profile,
        'vendor':vendor,
    }
    return render(request, 'vendors/vprofile.html', context)


def menu_builder(request):
    # vendor = get_vendor(request)
    vendor = get_vendor(request)
    categories = Category.objects.filter(vendor=vendor).order_by('created_at')
    context = {
        'categories': categories,
    }
    return render(request, 'vendors/menu_builder.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def fooditems_by_category(request, pk=None):
    vendor = get_vendor(request)
    category = get_object_or_404(Category, pk=pk)
    fooditems = FoodItem.objects.filter(vendor=vendor, category=category)
    context = {
        'fooditems': fooditems,
        'category': category,
    }
    return render(request, 'vendors/fooditems_by_category.html', context)

