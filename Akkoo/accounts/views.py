from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm
from vendors.forms import VendorForm
from .models import User, UserProfile
from django.contrib import messages
from django.contrib import auth
from .utils import detectUser, send_verification_email

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied


#Access control based on user type for vendors
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


#Access control for customers
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied


#register vendor
def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Already logged in')
        return redirect('myAccount')

    elif request.method == "POST":
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
            #Send email
            send_verification_email(request, user)
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

    if request.user.is_authenticated:
        messages.warning(request, 'Already logged in')
        return redirect('myAccount')

    elif request.method == 'POST':
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

            #Send email
            send_verification_email(request, user)
            messages.success(request, "Account Created Successfully!")
            
            return redirect('registerUser')
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)


def login(request):
    
    if request.user.is_authenticated:
        messages.warning(request, 'Already logged in')
        return redirect('myAccount')

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged In')
            return redirect('myAccount')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('login')


@login_required(login_url='login')
def myAccount(request):
    user = request.user
    # print(user)
    redirectUrl = detectUser(user)
    # print(f"REDIRECT******************))))**(*(&(&( + {redirectUrl}")
    return redirect(redirectUrl)


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def custDashboard(request):
    return render(request, 'accounts/custDashboard.html')


@user_passes_test(check_role_vendor)
@login_required(login_url='login')
def venDashboard(request):
    return render(request, 'accounts/venDashboard.html')


def activateAccount(request, uidb64, token):
    print("*************-------Account Activation-------**************")
    return