from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm
from vendors.forms import VendorForm
from .models import User, UserProfile
from django.contrib import messages

# Create your views here.


def registerVendor(request):

    if request.method == "POST":
        #get the user data
        form = UserForm(request.POST)
        
        #get the vendor data
        vendorForm = VendorForm(request.POST, request.FILES)
        
        #check if its valid and save it or show error
        if form.is_valid() and vendorForm.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # vendor_name = form.cleaned_data['vendor_name']
            # vendor_licence = form.cleaned_data['']

            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = user.VENDOR
            user.save()

            vendor = vendorForm.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, "Vendor has been registered successfully!")
        else:
            print(form.errors)
    form = UserForm()
    vendorForm = VendorForm()

    context = {
        'form': form,
        'vendorForm' : vendorForm
    }
    return render(request, 'accounts/registerVendor.html', context)

def registerUser(request):  
    # return HttpResponse("User Registration")
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # #1 Saving the password using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = user.CUSTOMER
            # form.save()
            # return redirect('registerUser')
            
            # #2 Saving the password using the create_user method we made in the User model
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Account Created Successfully!")
            
            return redirect('registerUser')
    
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)