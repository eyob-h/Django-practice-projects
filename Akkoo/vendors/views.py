from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vprofile(request):
    # user

    return render(request, 'vendors/vprofile.html')