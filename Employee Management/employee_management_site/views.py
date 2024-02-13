from django.http import HttpResponse
from django.shortcuts import render
# from django.http import *

def home(request):
    # return HttpResponse("hi home")
    return render(request, 'home.html')