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
