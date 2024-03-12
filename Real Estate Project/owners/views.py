from django.shortcuts import render, HttpResponse

# Create your views here.

def view_owners(request):
    return HttpResponse("Owner List")