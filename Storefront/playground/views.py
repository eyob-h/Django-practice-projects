from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#views in django= Request handlers
#req->res

#Say hi
def sayHi(request):
    return HttpResponse("Hi")